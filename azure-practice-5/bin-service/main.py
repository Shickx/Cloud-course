from fastapi import FastAPI
from services.chef_service import router

app = FastAPI()

app.include_router(router)