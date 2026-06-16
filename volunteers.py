from database import get_connection

def add_volunteer(name, phone, role):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO volunteers (name, phone, role) VALUES (?, ?, ?)", (name, phone, role))
    conn.commit()
    conn.close()

def view_volunteers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM volunteers")
    rows = cursor.fetchall()
    conn.close()
    return rows
