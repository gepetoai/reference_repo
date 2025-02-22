# import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.clients.db.postgres_client import Base, engine
from app.monitoring.logging import get_logger
from fastapi.responses import JSONResponse



logger = get_logger('main')

Base.metadata.create_all(bind= engine)

# App Setup
app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(healthRouter, prefix=settings.API_V1_STR)



@app.get("/health")
async def root():
    try:
        return JSONResponse(content={"message": "Hello Universe"})
    except Exception as e:
        logger.error(f"Error: {e}")
        return JSONResponse(status_code=500, content={"message": "Error"})