from fastapi import FastAPI

from app import models
from app.database import engine, Base
from app.routers.users import router as users_router

app = FastAPI(
    title="Calendar.io API",
    description="API for Calendar.io application",
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(users_router)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}
