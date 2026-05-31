import sqlite3

DB_NAME = "jobs.db"

def get_connection():
    conn = sqlite3.connect(
        DB_NAME,
        check_same_thread=False,
        timeout=30
    )
    return conn