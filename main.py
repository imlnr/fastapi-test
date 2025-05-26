from fastapi import FastAPI
from routes import users_routes

app = FastAPI()

# MongoDB connection
app.include_router(users_routes.router, tags=["users"])