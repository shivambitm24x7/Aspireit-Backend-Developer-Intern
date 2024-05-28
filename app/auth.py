from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import create_user, get_user
from app import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if get_user(data['username']):
        return jsonify({'message': 'User already exists'}), 400
    create_user(data['username'], data['password'])
    return jsonify({'message': 'User created successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = get_user(data['username'])
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity={'username': user['username']})
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth.route('/profile', methods=['GET', 'PUT'])
@jwt_required()
def profile():
    username = get_jwt_identity()['username']
    user = get_user(username)
    if request.method == 'GET':
        return jsonify({'username': user['username']}), 200
    elif request.method == 'PUT':
        data = request.get_json()
        mongo.db.users.update_one({'username': username}, {'$set': data})
        return jsonify({'message': 'Profile updated successfully'}), 200
