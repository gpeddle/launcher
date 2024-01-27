import sqlite3
import json
import uuid
from pydantic import BaseModel

from data.abstract_repository import AbstractRepository
from models.display import Display


class DisplayRepository(AbstractRepository):
    def __init__(self, db_file):
        self.db_file = db_file

    def load_initial_data(self, initial_data_file):

        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Drop table if it exists
        cursor.execute("DROP TABLE IF EXISTS display")

        # Create table with the current schema
        # note that id is a uuid
        cursor.execute("""
        CREATE TABLE display (
            id TEXT PRIMARY KEY,
            name TEXT,
            description TEXT,
            web_app TEXT,
            status TEXT,
            api_key TEXT,
            challenge_code TEXT
        );
        """)

        conn.commit()
        conn.close()

        # Read initial data from JSON file and insert into the database
        with open(initial_data_file, 'r') as file:
            initial_data = json.load(file)
            for entry in initial_data:
                # Create a Display instance from the JSON data
                display = Display(**entry)
                # Insert the display into the database
                self.create(display)

    def get_all(self):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM display")
            rows = cursor.fetchall()
            return [Display.parse_obj(row) for row in rows]

    def get_by_id(self, id:str):
        with sqlite3.connect(self.db_file) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM display WHERE id=?", (id,))
            row = cursor.fetchone()
            return Display.parse_obj(row)

    def create(self, display: Display):

        if display.id is None:
            display.id = uuid.uuid4()

        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO display (id, name, description, web_app, status, api_key, challenge_code) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (str(display.id), display.name, display.description,
                display.web_app, display.status, display.api_key, display.challenge_code),
            )
            conn.commit()
            return display.id



    def update(self, display: Display):

        if display.id is None:
            raise ValueError("Display ID cannot be None.")

        if self.get_by_id(str(display.id)) is None:
            raise ValueError(f"Display with ID {display.id} does not exist.")

        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE display SET name=?, description= ?, web_app=?, status=?, api_key=?, challenge_code=? WHERE id=?",
                (display.name, display.description, display.web_app,
                 display.status, display.api_key, display.challenge_code, str(display.id)),
            )
            conn.commit()

    def delete(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM display WHERE id=?", (id,))
            conn.commit()
