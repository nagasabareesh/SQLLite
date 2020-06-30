import sqlite3
from code.user import User

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "Create Table users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)

connection.commit()

connection.close()