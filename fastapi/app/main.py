from fastapi import FastAPI
from app.database.db import initialize_db

import app.routers.router_items

app = FastAPI(
    title="Watches API",
    redoc_url="/",
)

@app.on_event("startup")
async def startup_event():
    initialize_db()

app.include_router(app.routers.router_items.router)