from fastapi import APIRouter
from pydantic import BaseModel
from db import get_connection

router = APIRouter()

PREFIX = "s20230535"
SCHEMA = f"{PREFIX}_classes"


class ClassCreate(BaseModel):
    classId: int
    title: str
    chefId: int
    date: str
    capacity: int


class BookingCreate(BaseModel):
    bookingId: int
    classId: int
    userId: int
    status: str


@router.get("/classes")
def get_classes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT classId, title, chefId, date, capacity FROM {SCHEMA}.class")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "classId": r[0],
            "title": r[1],
            "chefId": r[2],
            "date": str(r[3]),
            "capacity": r[4]
        }
        for r in rows
    ]


@router.post("/classes")
def create_class(c: ClassCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {SCHEMA}.class VALUES (?, ?, ?, ?, ?)",
        (c.classId, c.title, c.chefId, c.date, c.capacity)
    )

    conn.commit()
    conn.close()

    return c


@router.get("/classes/{class_id}/bookings")
def get_bookings(class_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT bookingId, classId, userId, status FROM {SCHEMA}.booking WHERE classId = ?",
        (class_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "bookingId": r[0],
            "classId": r[1],
            "userId": r[2],
            "status": r[3]
        }
        for r in rows
    ]


@router.post("/bookings")
def create_booking(b: BookingCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {SCHEMA}.booking VALUES (?, ?, ?, ?)",
        (b.bookingId, b.classId, b.userId, b.status)
    )

    conn.commit()
    conn.close()

    return b