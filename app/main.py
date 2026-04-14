from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import get_conn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/rooms")
def get_rooms():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, room_number, type, price FROM hotel_rooms")
        return cur.fetchall()

@app.get("/bookings")
def get_bookings():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT b.id, r.room_number, b.datefrom, b.addinfo
            FROM hotel_bookings b
            JOIN hotel_rooms r ON b.room_id = r.id
        """)
        return cur.fetchall()

@app.post("/bookings")
def create_booking(data: dict):
    if data["date"] == "":
        return {"msg": "datum saknas"}

    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO hotel_bookings (guest_id, room_id, datefrom, dateto, addinfo)
            VALUES (1, %s, %s, %s, %s)
        """, (data["room_id"], data["date"], data["date"], data["addinfo"]))

    return {"msg": "saved"}