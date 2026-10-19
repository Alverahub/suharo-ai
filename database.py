import sqlite3
from pathlib import Path
from .config import DATABASE_PATH

def connect():
    p = Path(DATABASE_PATH)
    if p.parent != Path("."):
        p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect() as db:
        db.execute("CREATE TABLE IF NOT EXISTS reminders (id INTEGER PRIMARY KEY AUTOINCREMENT, label TEXT NOT NULL, time TEXT NOT NULL)")
        if db.execute("SELECT COUNT(*) FROM reminders").fetchone()[0] == 0:
            db.executemany("INSERT INTO reminders(label,time) VALUES (?,?)", [("Morning routine (demo)", "08:00"), ("Drink water", "10:00")])

def all_reminders():
    with connect() as db:
        return [dict(r) for r in db.execute("SELECT id,label,time FROM reminders ORDER BY time,id").fetchall()]

def create_reminder(label, time):
    with connect() as db:
        cur = db.execute("INSERT INTO reminders(label,time) VALUES (?,?)", (label, time))
        return dict(db.execute("SELECT id,label,time FROM reminders WHERE id=?", (cur.lastrowid,)).fetchone())

def remove_reminder(item_id):
    with connect() as db:
        return db.execute("DELETE FROM reminders WHERE id=?", (item_id,)).rowcount > 0
