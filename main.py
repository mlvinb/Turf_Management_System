import mysql.connector
from datetime import datetime

# --------------------- Database Connection ---------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="1309",  # change to your MySQL password
        database="turf_management"
    )

# --------------------- Admin Functions ---------------------
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
    data = cur.fetchone()

    if data:
        print("\nAdmin login successful!\n")
        admin_menu()
    else:
        print("\nInvalid admin credentials!\n")
    con.close()


def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. View All Turfs")
        print("2. Add Turf")
        print("3. View All Bookings")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            view_turfs()
        elif choice == '2':
            add_turf()
        elif choice == '3':
            view_bookings()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice!")


def view_turfs():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM turf")
    data = cur.fetchall()

    print("\n--- TURF LIST ---")
    for row in data:
        print(f"Turf ID: {row[0]}, Name: {row[1]}, Location: {row[2]}, Price/hr: ₹{row[3]}, Type: {row[4]}")
    con.close()


def add_turf():
    name = input("Enter turf name: ")
    location = input("Enter location: ")
    price = float(input("Enter price per hour: "))
    turf_type = input("Enter turf type (Football/Cricket/etc): ")

    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO turf (turf_name, location, price_per_hour, turf_type, availability) VALUES (%s, %s, %s, %s, 'Available')",
                (name, location, price, turf_type))
    con.commit()
    con.close()
    print("\nTurf added successfully!")


def view_bookings():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM booking")
    data = cur.fetchall()
    print("\n--- ALL BOOKINGS ---")
    for row in data:
        print(f"Booking ID: {row[0]}, User ID: {row[1]}, Turf ID: {row[2]}, Date: {row[3]}, Time: {row[4]} - {row[5]}, Status: {row[6]}")
    con.close()

# --------------------- User Functions ---------------------
def user_signup():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    con.commit()
    con.close()
    print("\nSignup successful! You can now log in.\n")


def user_login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    data = cur.fetchone()

    if data:
        print("\nLogin successful!\n")
        user_menu(data[0])  # pass user_id
    else:
        print("\nInvalid credentials!\n")
    con.close()


def user_menu(user_id):
    while True:
        print("\n--- USER MENU ---")
        print("1. View Available Turfs")
        print("2. Book Turf")
        print("3. View My Bookings")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            view_turfs()
        elif choice == '2':
            book_turf(user_id)
        elif choice == '3':
            view_my_bookings(user_id)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice!")

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

# --------------------- Main Menu ---------------------
def main_menu():
    while True:
        print("\n=== TURF MANAGEMENT SYSTEM ===")
        print("1. Admin Login")
        print("2. User Login")
        print("3. User Signup")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            admin_login()
        elif choice == '2':
            user_login()
        elif choice == '3':
            user_signup()
        elif choice == '4':
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")

# --------------------- Run App ---------------------
main_menu()
