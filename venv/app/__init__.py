from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://shivambitm24x7:5R6suDuEn2VBcDxd@shivambitm.2qz4q59.mongodb.net/?retryWrites=true&w=majority&appName=shivambitm'
app.config['JWT_SECRET_KEY'] = 't45e65r76fyg978h'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from app import routes, auth, ml

if __name__ == '__main__':
    app.run(debug=True)

