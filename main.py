'#type:ignore'
from fastapi import FastAPI # type: ignore
from mangum import Mangum # type: ignore

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def read_root():
    return {"message": "Hello, this is my first FastAPI app running on AWS Lambda with Mangum!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}