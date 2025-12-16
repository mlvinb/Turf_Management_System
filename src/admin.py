# --------------------- Connections ---------------------
from .db import connect_db

from datetime import datetime

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