from user import User

def authenticate(username, password):
    user = User.find_user_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_user_by_id(_id=user_id)