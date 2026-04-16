from fastapi import FastAPI

from services.chef_service import router as chef_router
from services.class_service import router as class_router
from services.feedback_service import router as feedback_router

app = FastAPI()

app.include_router(chef_router)
app.include_router(class_router)
app.include_router(feedback_router)