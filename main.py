import imp
from fastapi import FastAPI

app = FastAPI()  # created instance of fastAPI

# fast operation  removed async name itself doesnt matter


@app.get("/")  # decorator  http mrthod: get  root path: "/"
def root():
    return {"message": "Hello World!!!"}  # dictionary to json


@app.get("/posts")
def get_posts():
    return {"data": "this is your posts"}


@app.post("/createposts")
def create_posts():
    return {"message": "successfully created posts"}
