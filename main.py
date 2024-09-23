from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


# Pydantic models
class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # is optional and defaults to true
    rating: Optional[int] = None  # optional but without default


my_posts = [
    {
        "title": "Title of the post",
        "content": "This is the content of the post",
        "published": False,
        "rating": None,
        "id": 1,
    },
    {
        "title": "Title of the second post",
        "content": "This is the content of the second post",
        "published": False,
        "rating": None,
        "id": 2,
    },
]


# request Get method URL: "/"
@app.get("/")
def read_root():
    return {"Hello": "World"}


# request Get method URL: "/posts"
@app.get("/posts")
def get_posts():
    return {"data": my_posts}  # automatically serializes array into JSON


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 100000)  # Temporarily add id until DB does it
    # print(post.model_dump()) # # This converts the pydantic model into a dictionary
    my_posts.append(post_dict)

    return {"data": post_dict}
