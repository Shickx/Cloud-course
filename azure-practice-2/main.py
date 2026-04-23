from fastapi import FastAPI

from services.chef_service import router as chef_router
from services.class_service import router as class_router
from services.feedback_service import router as feedback_router
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

app.include_router(chef_router)
app.include_router(class_router)
app.include_router(feedback_router)

@app.on_event("startup")
def start_listener():
    import threading
    from services.queue_listener import listen_queue

    thread = threading.Thread(target=listen_queue, daemon=True)
    thread.start()