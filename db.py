# --------------------- Database Connection ---------------------

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change if needed
        password="1309",  # change to your MySQL password
        database="turf_management"
    )