import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_user_by_username(cls, username):
        connect = sqlite3.connect("data.db")
        cursor = connect.cursor()

        select_query = "select * from users where username=?"
        result_user = cursor.execute(select_query, (username,))
        row = result_user.fetchone()
        print(result_user)
        if row:
            user = cls(*row)
        else:
            user = None

        return user

    @classmethod
    def find_user_by_id(cls, _id):
        connect = sqlite3.connect("data.db")
        cursor = connect.cursor()

        select_query = "select * from users where id=?"
        result_user = cursor.execute(select_query, (_id,))
        row = result_user.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This is mandatory field")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This is mandatory field")

    def post(self):
        data = UserRegister.parser.parse_args()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        select_query = "select username from users where username = ?"
        result_query = cursor.execute(select_query,(data['username'],))
        row = result_query.fetchone()
        if row:
            return {'User creation': 'user already exists'}


        insert_query = "insert into users values (NULL, ?, ?)"
        cursor.execute(insert_query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {'User creation':'User created successfully'}

