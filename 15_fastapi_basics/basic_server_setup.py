
# Importing the FastAPI
from fastapi import FastAPI

# Creating the app
app = FastAPI()

# Creating get / api which return the dict
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Creating a dynamic route of /item/{item_id} which return the dict of dynamic id
@app.get("/item/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}