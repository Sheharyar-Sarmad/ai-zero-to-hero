"""
Tests for working_with_db.py.   Run:  pytest -v

By default the tests use an in-memory SQLite database (no server needed).
To test against real PostgreSQL, point at a THROWAWAY database (tables are dropped after each test):
    TEST_DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/ai_zero_to_hero_test pytest -v
"""
import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import working_with_db as app_module
from working_with_db import Base, app, get_db

TEST_URL = os.getenv("TEST_DATABASE_URL", "sqlite://")


@pytest.fixture()
def client():
    kwargs = {"poolclass": StaticPool, "connect_args": {"check_same_thread": False}} if TEST_URL.startswith("sqlite") else {}
    engine = create_engine(TEST_URL, **kwargs)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

    def override_get_db():
        with Session() as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)  # no "with": skips lifespan, so the real database is never touched
    app.dependency_overrides.clear()
    Base.metadata.drop_all(engine)
    engine.dispose()


def make(client, title, **extra):
    return client.post("/tasks", json={"title": title, **extra})


def test_create_returns_201_with_defaults(client):
    r = make(client, "  Learn SQL  ")
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "Learn SQL" and body["priority"] == "medium" and body["done"] is False
    assert body["id"] == 1 and body["created_at"] and body["updated_at"]


def test_duplicate_title_is_409_case_insensitive(client):
    assert make(client, "Learn SQL").status_code == 201
    assert make(client, "learn sql").status_code == 409


@pytest.mark.parametrize("payload", [{"title": ""}, {"title": "   "}, {"title": "x" * 101}, {"title": "ok", "priority": "urgent"}, {}])
def test_invalid_input_is_422(client, payload):
    assert client.post("/tasks", json=payload).status_code == 422


def test_bulk_create_is_atomic(client):
    ok = client.post("/tasks/bulk", json=[{"title": "A"}, {"title": "B", "priority": "high"}])
    assert ok.status_code == 201 and [t["title"] for t in ok.json()] == ["A", "B"]
    bad = client.post("/tasks/bulk", json=[{"title": "C"}, {"title": "a"}])  # "a" duplicates "A"
    assert bad.status_code == 409
    assert [t["title"] for t in client.get("/tasks").json()] == ["A", "B"]  # "C" was rolled back
    assert client.post("/tasks/bulk", json=[]).status_code == 422


def test_list_filters_search_and_pagination(client):
    make(client, "Write report", priority="high")
    make(client, "Read book", priority="low")
    make(client, "Write tests", priority="high")
    client.patch("/tasks/1", json={"done": True})

    assert len(client.get("/tasks?q=WRITE").json()) == 2
    assert [t["id"] for t in client.get("/tasks?priority=low").json()] == [2]
    assert [t["id"] for t in client.get("/tasks?done=true").json()] == [1]
    page = client.get("/tasks?skip=1&limit=1")
    assert [t["id"] for t in page.json()] == [2] and page.headers["x-total-count"] == "3"
    assert client.get("/tasks?q=write&limit=1").headers["x-total-count"] == "2"
    assert client.get("/tasks?q=100%").json() == []  # % is escaped, not a wildcard
    assert client.get("/tasks?limit=0").status_code == 422
    assert client.get("/tasks?priority=nope").status_code == 422


def test_stats(client):
    assert client.get("/tasks/stats").json() == {"total": 0, "done": 0, "pending": 0, "by_priority": {}}
    make(client, "A", priority="high"); make(client, "B", priority="high"); make(client, "C", priority="low")
    client.patch("/tasks/1", json={"done": True})
    assert client.get("/tasks/stats").json() == {"total": 3, "done": 1, "pending": 2, "by_priority": {"high": 2, "low": 1}}


def test_read_patch_and_404(client):
    make(client, "A"); make(client, "B")
    assert client.get("/tasks/1").status_code == 200
    assert client.get("/tasks/99").status_code == 404
    r = client.patch("/tasks/1", json={"done": True, "priority": "high"})
    assert r.status_code == 200 and r.json()["done"] is True and r.json()["priority"] == "high"
    assert client.patch("/tasks/1", json={"done": None}).json()["done"] is True  # null is ignored, no 500
    assert client.patch("/tasks/2", json={"title": "a"}).status_code == 409
    assert client.patch("/tasks/99", json={"done": True}).status_code == 404
    assert client.get("/tasks/abc").status_code == 422


def test_delete_204_then_404(client):
    make(client, "A")
    r = client.delete("/tasks/1")
    assert r.status_code == 204 and r.content == b""
    assert client.delete("/tasks/1").status_code == 404
    assert client.get("/tasks/1").status_code == 404


def test_health_up_and_503_when_database_is_down(client):
    assert client.get("/health/db").json() == {"database": "up"}

    class DownSession:
        def execute(self, *_):
            raise OperationalError("SELECT 1", {}, Exception("connection refused"))

    def broken():
        yield DownSession()

    app.dependency_overrides[get_db] = broken
    r = client.get("/health/db")
    assert r.status_code == 503 and "unavailable" in r.json()["detail"]


def test_engine_uses_pooling_options():
    assert app_module.engine.pool.size() == 5