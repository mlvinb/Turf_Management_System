# --------------------- Connections ---------------------
from .db import connect_db
from datetime import datetime
from .admin import view_turfs

from datetime import datetime

# --------------------- Booking Functions ---------------------
def book_turf(user_id):
    view_turfs()
    turf_id = input("Enter Turf ID to book: ")

    date_input = input("Enter booking date (DD/MM/YYYY): ")
    try:
        date = datetime.strptime(date_input, "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use DD/MM/YYYY.")
        return

    start_time = input("Enter start time (24-hr format HH:MM, e.g. 17:00): ")
    end_time = input("Enter end time (24-hr format HH:MM, e.g. 19:00): ")

    # Validate time format
    try:
        datetime.strptime(start_time, "%H:%M")
        datetime.strptime(end_time, "%H:%M")
    except ValueError:
        print("Invalid time format! Use HH:MM (24-hour).")
        return

    con = connect_db()
    cur = con.cursor()

    # Check if turf already booked for same date and time
    cur.execute("""
        SELECT * FROM booking 
        WHERE turf_id=%s AND date=%s 
        AND ((start_time <= %s AND end_time > %s) OR (start_time < %s AND end_time >= %s))
        AND status='Booked'
    """, (turf_id, date, start_time, start_time, end_time, end_time))
    conflict = cur.fetchone()

    if conflict:
        print("\nTurf is already booked for that time slot!")
    else:
        cur.execute("""
            INSERT INTO booking (user_id, turf_id, date, start_time, end_time, status)
            VALUES (%s, %s, %s, %s, %s, 'Booked')
        """, (user_id, turf_id, date, start_time, end_time))
        con.commit()
        print("\nBooking confirmed!")
    con.close()


def view_my_bookings(user_id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM booking WHERE user_id=%s", (user_id,))
    data = cur.fetchall()

    print("\n--- MY BOOKINGS ---")
    for row in data:
        print(f"Booking ID: {row[0]}, Turf ID: {row[2]}, Date: {row[3]}, Time: {row[4]} - {row[5]}, Status: {row[6]}")
    con.close()