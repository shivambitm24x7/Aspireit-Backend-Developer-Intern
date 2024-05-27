from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/aspireit'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from app import routes, auth, ml

if __name__ == '__main__':
    app.run(debug=True)
