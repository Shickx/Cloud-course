from fastapi import FastAPI
from services.feedback_service import router

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def start_listener():
    import threading
    from services.queue_listener import listen_queue

    thread = threading.Thread(target=listen_queue, daemon=True)
    thread.start()