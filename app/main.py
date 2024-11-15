# app/main.py
from fastapi import FastAPI
from app.api.endpoints import user
from app.core.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# Include router untuk endpoint user
app.include_router(user.router)
# app.include_router(user.router, prefix="/api/users", tags=["users"])




