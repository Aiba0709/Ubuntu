# SQL - Structured Query Language (язык структуриемых запросов)
# СУБД - Система управления базой данных

# SQLite (СУБД)

import sqlite3

def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE students("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "fullname VARCHAR (200) NOT NULL,"
        "mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,"
        "hobby TEXT DEFOULT NULL,"
        "birth_date DATE NOT NULL,"
        "is_married BOOLEAN DEFOULT FALSE)"
    )
    conn.commit()

connection = create_connection("my_db.db")  

if connection is not None:
    print("Conneted!")
    create_table(connection)