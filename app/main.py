from fastapi import FastAPI
from app.interfaces.routes import auth_router

app = FastAPI()

app.include_router(auth_router.router)

@app.get("/")
def read_root():
    return {"message": "Hello, Leave Management System!"}