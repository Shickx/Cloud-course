from fastapi import APIRouter
from pydantic import BaseModel
from db import get_connection

router = APIRouter()

SCHEMA = "MikitaMalafei"


class ChefCreate(BaseModel):
    chefId: int
    name: str
    rating: float


@router.get("/chefs")
def get_chefs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT chefId, name, rating FROM {SCHEMA}.chef")
    rows = cursor.fetchall()

    conn.close()

    return [{"chefId": r[0], "name": r[1], "rating": r[2]} for r in rows]


@router.get("/chefs/{chef_id}")
def get_chef(chef_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT chefId, name, rating FROM {SCHEMA}.chef WHERE chefId = ?",
        (chef_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"error": "not found"}

    return {"chefId": row[0], "name": row[1], "rating": row[2]}


@router.post("/chefs")
def create_chef(chef: ChefCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {SCHEMA}.chef VALUES (?, ?, ?)",
        (chef.chefId, chef.name, chef.rating)
    )

    conn.commit()
    conn.close()

    return chef