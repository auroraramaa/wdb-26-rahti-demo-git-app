from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# tillfällig "databas"
temp_rooms = [
    {"room_number": 101, "room_type": "Double room", "price": 100},
    {"room_number": 202, "room_type": "Single room", "price": 80},
    {"room_number": 303, "room_type": "Suite", "price": 500}
]

@app.get("/")
def read_root():
    return {"msg": "Välkommen till hotellets boknings-API"}

@app.get("/rooms")
def rooms():
    return temp_rooms

@app.post("/bookings")
def create_booking():
    return {"msg": "Bokning skapad!"}