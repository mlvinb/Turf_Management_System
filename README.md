# Turf Management System

A **console-based Turf Management System** developed using **Python and MySQL**, designed to manage turf bookings, users, and administrative operations through a database-driven approach. The project demonstrates Python–MySQL connectivity and core DBMS concepts in a practical application.

---

## 📌 Features

### Admin Features

* Secure admin login
* Add new turfs with details (name, location, price, type)
* View all registered turfs
* View all bookings made by users

### User Features

* User signup and login
* View available turfs
* Book turfs for a selected date and time
* Automatic prevention of double bookings
* View personal booking history

### System Features

* MySQL database integration using `mysql-connector-python`
* Structured relational database design
* Validation of date and time inputs
* Modular Python codebase for maintainability

---

## 🎯 Objectives of the Project

The main objective of the Turf Management System is to provide an efficient and user-friendly platform to manage turf bookings and customer records digitally.

Specific objectives include:

* Digitalizing turf management by maintaining customer and booking records in a structured database
* Simplifying the booking process by allowing quick confirmation of available time slots
* Enabling administrators to add and manage turf details easily
* Preventing double bookings by validating turf availability before confirmation
* Demonstrating real-world database connectivity between Python and MySQL
* Automating turf management operations to improve accuracy and efficiency

---

## 🛠️ Technologies Used

* **Python 3**
* **MySQL**
* **mysql-connector-python**
* Console-based interface (CLI)

---

## 📂 Project Structure

```
Turf-Management-System/
├── src/
│   ├── __init__.py
│   ├── main.py          # Entry point of the application
│   ├── db.py            # MySQL database connection logic
│   ├── admin.py         # Admin-related operations
│   ├── user.py          # User management functions
│   └── booking.py       # Turf booking and availability logic
│
├── sql/
│   ├── schema.sql       # Database schema (tables & constraints)
│   ├── insert_data.sql  # Sample INSERT queries
│   └── queries.sql      # Business/analysis SQL queries
│
├── README.md
├── .gitignore
└── LICENSE

```

---

## ⚙️ Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/your-username/turf-management-system.git
cd turf-management-system
```

2. Create the database

* Open MySQL
* Run the SQL file:

```sql
source schema.sql;
```

3. Install required package

```bash
pip install mysql-connector-python
```

4. Update database credentials in `db.py`

```python
user="root"
password="your_password"
database="turf_management"
```

5. Run the application

```bash
python main.py
```

---

## 🚀 Future Enhancements

* Password hashing for better security
* Payment and revenue management
* Report generation
* GUI or web-based interface

---

## 📌 Notes

* This project focuses on core DBMS concepts and backend logic
* Designed to be simple, modular, and easy to understand

---

## 📄 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this project with proper attribution.

