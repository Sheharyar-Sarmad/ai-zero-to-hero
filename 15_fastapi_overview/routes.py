"""
routes.py - FastAPI routes with explicit HTTP status codes.

Run:   uvicorn routes:app --reload
Docs:  http://127.0.0.1:8000/docs

Status codes used in this file
  200 OK                    read or update succeeded
  201 Created               POST created a resource (Location header points to it)
  204 No Content            DELETE succeeded, nothing to return
  401 Unauthorized          credentials missing (who are you?)
  403 Forbidden             credentials present but not allowed (you may not)
  404 Not Found             the id does not exist
  409 Conflict              duplicate resource / state clash
  422 Unprocessable Entity  automatic: body or params failed Pydantic validation
"""
import os
import secrets
from itertools import count

from fastapi import APIRouter, Depends, FastAPI, Header, HTTPException, Path, Query, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Routes and Status Codes")
router = APIRouter(prefix="/items", tags=["items"])


# Schemas (Pydantic validates input and shapes output) 
class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0)
    in_stock: bool = True


class ItemUpdate(BaseModel):  # PATCH: every field optional
    name: str | None = Field(default=None, min_length=1, max_length=50)
    price: float | None = Field(default=None, gt=0)
    in_stock: bool | None = None


class Item(ItemCreate):
    id: int


# In-memory "database" (see working_with_db.py for a real one) 
_items: dict[int, Item] = {}
_next_id = count(1)


def get_or_404(item_id: int) -> Item:
    item = _items.get(item_id)
    if item is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found")
    return item


def name_taken(name: str, ignore_id: int | None = None) -> bool:
    return any(i.name.lower() == name.lower() and i.id != ignore_id for i in _items.values())


# Item routes 
@router.get("", response_model=list[Item])  # 200 is the default for GET
def list_items(
    search: str | None = Query(default=None, description="filter by name"),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
):
    items = [i for i in _items.values() if not search or search.lower() in i.name.lower()]
    return items[skip : skip + limit]


@router.get("/{item_id}", response_model=Item, responses={404: {"description": "Item not found"}})
def read_item(item_id: int = Path(ge=1)):
    return get_or_404(item_id)


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED,
             responses={409: {"description": "Name already exists"}})
def create_item(body: ItemCreate, response: Response):
    if name_taken(body.name):
        raise HTTPException(status.HTTP_409_CONFLICT, detail=f"Item '{body.name}' already exists")
    item = Item(id=next(_next_id), **body.model_dump())
    _items[item.id] = item
    response.headers["Location"] = f"/items/{item.id}"  # where the new resource lives
    return item


@router.put("/{item_id}", response_model=Item)  # replace the whole resource
def replace_item(body: ItemCreate, item_id: int = Path(ge=1)):
    get_or_404(item_id)
    if name_taken(body.name, ignore_id=item_id):
        raise HTTPException(status.HTTP_409_CONFLICT, detail=f"Item '{body.name}' already exists")
    _items[item_id] = Item(id=item_id, **body.model_dump())
    return _items[item_id]


@router.patch("/{item_id}", response_model=Item)  # change only the fields that were sent
def update_item(body: ItemUpdate, item_id: int = Path(ge=1)):
    item = get_or_404(item_id)
    changes = body.model_dump(exclude_unset=True)
    if "name" in changes and name_taken(changes["name"], ignore_id=item_id):
        raise HTTPException(status.HTTP_409_CONFLICT, detail=f"Item '{changes['name']}' already exists")
    _items[item_id] = item.model_copy(update=changes)
    return _items[item_id]


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int = Path(ge=1)):
    get_or_404(item_id)
    del _items[item_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)  # 204 must have no body


# 401 vs 403 
API_KEY = os.getenv("API_KEY", "dev-key")  # demo only: load real secrets from .env


def require_api_key(x_api_key: str | None = Header(default=None)):
    if x_api_key is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Missing API key",
                            headers={"WWW-Authenticate": "ApiKey"})
    if not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid API key")


@app.get("/admin/stats", tags=["admin"], dependencies=[Depends(require_api_key)])
def admin_stats():
    return {"total_items": len(_items), "in_stock": sum(i.in_stock for i in _items.values())}


# Health + a status-code playground 
@app.get("/", tags=["meta"])
def health():
    return {"status": "ok"}


@app.get("/demo/status/{code}", tags=["meta"])
def demo_status(code: int = Path(ge=200, le=599)):
    """Try any code from 200 to 599 and watch how clients and /docs react."""
    if code in (204, 205, 304):  # these must not carry a body
        return Response(status_code=code)
    if code >= 400:
        raise HTTPException(code, detail=f"Demo error {code}")
    return Response(content=f'{{"status": {code}}}', status_code=code, media_type="application/json")


app.include_router(router)