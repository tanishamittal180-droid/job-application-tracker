import sqlite3

conn = sqlite3.connect("jobs.db")
cur = conn.cursor()

# USERS TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

# APPLICATIONS TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    company TEXT,
    role TEXT,
    status TEXT,
    location TEXT,
    salary TEXT,
    apply TEXT,
    interview TEXT,
    resume TEXT,
    cover TEXT,
    notes TEXT,
    keywords TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully 🚀")