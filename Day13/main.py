from fastapi import FastAPI

from routes.user_route import routes


app = FastAPI(
    title="Day 1 Backend API",
    version="1.0.0"
)


app.include_router(
    routes,
    prefix="/api",
    tags=["Users"]
)