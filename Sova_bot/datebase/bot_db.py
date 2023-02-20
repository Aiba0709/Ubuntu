import sqlite3


# СУБД - Система управления базой данных
# SQL - Structured Query Language

def sql_create():
    global db, cursor
    db =  sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключенна!")

    db.execute("CREATE TABLE IF NOT EXISTS aibek"
              "(id INTEGER PRIMARI KEY, username TEXT,"
              "name TEXT, age INTEGER, gender TEXT," 
              "regin TEXT, photo TEXT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO aibek VALUES (?,?,?,?,?,?,?)", tuple(data.values()))
        db.commit()  

