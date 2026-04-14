import os
import psycopg

DATABASE_URL = os.getenv("DATABASE_URL")


def get_conn():
    return psycopg.connect(
        DATABASE_URL,
        autocommit=True,
        row_factory=psycopg.rows.dict_row
    )


def create_schema():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS hotel_rooms (
                id SERIAL PRIMARY KEY,
                room_number INT NOT NULL,
                type VARCHAR NOT NULL,
                price NUMERIC NOT NULL
            );

            CREATE TABLE IF NOT EXISTS hotel_guests (
                id SERIAL PRIMARY KEY,
                firstname VARCHAR NOT NULL,
                lastname VARCHAR NOT NULL,
                address VARCHAR NOT NULL
            );

            CREATE TABLE IF NOT EXISTS hotel_bookings (
                id SERIAL PRIMARY KEY,
                guest_id INT NOT NULL REFERENCES hotel_guests(id),
                room_id INT NOT NULL REFERENCES hotel_rooms(id),
                datefrom DATE NOT NULL,
                dateto DATE NOT NULL,
                addinfo VARCHAR
            );
        """)