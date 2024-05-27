from flask_pymongo import PyMongo

mongo = PyMongo()

def create_user(username, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = {
        'username': username,
        'password': hashed_password
    }
    mongo.db.users.insert_one(user)

def get_user(username):
    return mongo.db.users.find_one({'username': username})
