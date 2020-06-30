import sqlite3
from code.user import User

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "Create Table users (id int, username text, password text)"

cursor.execute(create_table)

users = [
        (2, "naga","sabareesh"),
        (3, "sabareesh", "naga")
]


user = (1, "jose", "asdf")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.executemany(insert_query, users)

select_query = "select * from users"

for row in cursor.execute(select_query):
        print(row)

connection.commit()

connection.close()