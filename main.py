from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
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


@app.post(
    "/posts", status_code=status.HTTP_201_CREATED
)  # this status will get send on response
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 100000)  # Temporarily add id until DB does it
    # print(post.model_dump()) # # This converts the pydantic model into a dictionary
    my_posts.append(post_dict)

    return {"data": post_dict}


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(int(id))

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # find the index in the array
    index = find_index_post(id)

    # if not founds - fail
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    # find the index in the array
    index = find_index_post(id)

    # if not founds - fail
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )
    post_dict = post.model_dump()
    post_dict["id"] = id
    my_posts[index] = post_dict

    return {"data": post_dict}
