from fastapi import FastAPI
from services.class_service import router

app = FastAPI()

app.include_router(router)