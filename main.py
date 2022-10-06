from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()  # created instance of fastAPI


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")  # decorator  http mrthod: get  root path: "/"
def root():
    return {"message": "Hello World!!!"}  # dictionary to json


@app.get("/posts")
def get_posts():
    return {"data": "this is your posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": "new post"}

    # def create_posts(payload: dict = Body(...)):
    # print(payload)
    # return {"message": "successfully created posts"}
    # return {"new_post": f"title {payload['title']} content: {payload['content']}"}
