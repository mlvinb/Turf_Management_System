# --------------------- Connections ---------------------
from admin import admin_login
from user import user_login, user_signup

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
