## FastAPI Basics

FastAPI is a modern and high-performance Python web framework used to build APIs and backend applications.
Its mainly work on pydantic dtypes so learning it is also very important and also you can research about it as well

## Installation

Install FastAPI using pip:

pip install fastapi

Install Uvicorn to run the FastAPI application:

pip install uvicorn
Creating the FastAPI Application

## The basic FastAPI application is created using:

app = FastAPI()

FastAPI() creates the FastAPI application instance.

The app variable represents the FastAPI application.

## Running the Server

If your Python file is named main.py and your FastAPI application is named app, run:

uvicorn main:app --reload
Command Breakdown
uvicorn — ASGI server used to run the FastAPI application.
main — the Python file main.py.
app — the FastAPI application instance.
--reload — automatically reloads the server when code changes during development.

The server will normally run at:

http://127.0.0.1:8000

FastAPI also provides automatic API documentation at:

http://127.0.0.1:8000/docs

and:

http://127.0.0.1:8000/redoc