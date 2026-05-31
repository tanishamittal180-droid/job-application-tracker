from database import get_connection

# ---------------- REGISTER ----------------
def register(name, email, password):

    email = email.strip().lower()
    password = password.strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cur.fetchone()

    if user:
        conn.close()
        return False

    cur.execute("""
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
    """, (name, email, password))

    conn.commit()
    conn.close()
    return True


# ---------------- LOGIN ----------------
def login(email, password):

    email = email.strip().lower()
    password = password.strip()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM users 
        WHERE email=? AND password=?
    """, (email, password))

    user = cur.fetchone()

    conn.close()

    return user