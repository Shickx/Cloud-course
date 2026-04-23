from fastapi import APIRouter
from pydantic import BaseModel
from db import get_connection
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os
router = APIRouter()

SCHEMA = "MikitaMalafei"
SEND_CONNECTION_STR = os.getenv("SERVICEBUS_SEND")
QUEUE_NAME = "mikitamalafei"

class FeedbackCreate(BaseModel):
    feedbackId: int
    classId: int
    rating: int
    comment: str


@router.get("/feedbacks")
def get_feedbacks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT feedbackId, classId, rating, comment FROM {SCHEMA}.feedback")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"feedbackId": r[0], "classId": r[1], "rating": r[2], "comment": r[3]}
        for r in rows
    ]


@router.post("/feedbacks")
def create_feedback(f: FeedbackCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {SCHEMA}.feedback VALUES (?, ?, ?, ?)",
        (f.feedbackId, f.classId, f.rating, f.comment)
    )
    send_message_to_queue(f"New feedback: {f.comment}")

    conn.commit()
    conn.close()

    return f

def send_message_to_queue(message: str):
    with ServiceBusClient.from_connection_string(SEND_CONNECTION_STR) as client:
        sender = client.get_queue_sender(queue_name=QUEUE_NAME)
        with sender:
            sender.send_messages(ServiceBusMessage(message))