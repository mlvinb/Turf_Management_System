# --------------------- Connections ---------------------
from db import connect_db
from booking import book_turf, view_my_bookings
from admin import view_turfs


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