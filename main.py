from fastapi import FastAPI

app = FastAPI()


# request Get method URL: "/"
@app.get("/")
def read_root():
    return {"Hello": "World"}


# request Get method URL: "/posts"
@app.get("/posts")
def get_posts():
    return {"data": "This is a list posts"}
