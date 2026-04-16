from fastapi import APIRouter
from pydantic import BaseModel
from db import get_connection

router = APIRouter()

PREFIX = "s20230535"
SCHEMA = f"{PREFIX}_feedbacks"


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

    conn.commit()
    conn.close()

    return f