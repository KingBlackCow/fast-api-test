from fastapi import FastAPI
from app.exceptions.exception_handler import register_exception_handlers
from app.routes import user_controller

app = FastAPI()
app.include_router(user_controller.router)
register_exception_handlers(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
