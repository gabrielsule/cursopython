import sqlite3
import json
from pathlib import Path

data = json.loads(Path("data.json").read_text())

with sqlite3.connect("data.sqlite3") as conn:
    comm = "INSERT INTO data VALUES (?, ?)"
    for d in data:
        conn.execute(comm, tuple(d.values()))
    conn.commit()

with sqlite3.connect("data.sqlite3") as conn:
    comm = "SELECT * FROM data"
    cursor = conn.execute(comm)
    for c in cursor:
        print(c)
    conn.commit()