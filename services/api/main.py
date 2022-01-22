from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/blog/{blog_id}")
def get_blog(blog_id: int):
    return {"message": f"Blog with id {blog_id}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
