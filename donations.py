from database import get_connection

def add_donation(donor_name, amount_or_item):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donations (donor_name, amount_or_item) VALUES (?, ?)", (donor_name, amount_or_item))
    conn.commit()
    conn.close()

def view_donations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donations")
    rows = cursor.fetchall()
    conn.close()
    return rows
