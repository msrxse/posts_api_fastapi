from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic models
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # is optional and defaults to true
    rating: Optional[int] = None  # optional but without default


# request Get method URL: "/"
@app.get("/")
def read_root():
    return {"Hello": "World"}


# request Get method URL: "/posts"
@app.get("/posts")
def get_posts():
    return {"data": "This is a list posts"}


@app.post("/createposts")
def create_post(post: Post):
    print(post.model_dump())  # This converts the pydantic model into a dictionary
    return {"data": post}
