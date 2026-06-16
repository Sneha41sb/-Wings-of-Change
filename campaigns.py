from database import get_connection

def log_campaign(event_name, location, beneficiaries_reached):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO campaigns (event_name, location, beneficiaries_reached) VALUES (?, ?, ?)", 
                   (event_name, location, beneficiaries_reached))
    conn.commit()
    conn.close()

def view_campaigns():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM campaigns")
    rows = cursor.fetchall()
    conn.close()
    return rows
