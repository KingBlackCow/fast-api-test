from fastapi import FastAPI
from app.routes import user_controller
from app import models
app = FastAPI()
app.include_router(user_controller.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
