from database import get_connection

# ---------------- ADD ----------------
from database import get_connection

def add_app(data):

    conn = get_connection()
    cur = conn.cursor()

    # SAFE INSERT (12 columns ONLY)
    cur.execute("""
        INSERT INTO applications
        (user, company, role, status, location,
         salary, apply, interview, resume,
         cover, notes, keywords)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data[:12])   # 👈 IMPORTANT FIX

    conn.commit()
    conn.close()

# ---------------- GET ----------------
def get_apps(user):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM applications WHERE user=?", (user,))
    rows = cur.fetchall()

    conn.close()
    return rows


# ---------------- DELETE ----------------
def delete_app(app_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM applications WHERE id=?", (app_id,))
    conn.commit()
    conn.close()


# ---------------- UPDATE STATUS ----------------
def update_status(app_id, status):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE applications SET status=? WHERE id=?",
        (status, app_id)
    )

    conn.commit()
    conn.close()