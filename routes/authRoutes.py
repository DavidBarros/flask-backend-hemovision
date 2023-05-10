from flask import Blueprint, jsonify, request
from modelos.user import User
from services.auth_service import AuthService

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/register', methods=['POST'])
def register():

    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    birthDate = request.json.get("birthDate")
    email = request.json.get("email")
    password = request.json.get("password")

    user = User(firstName=firstName, lastName=lastName,
                birthDate=birthDate, email=email, password=password)
    try:
        registeredUser = AuthService.createUser(user)
        registeredUser._id = str(registeredUser._id)
        return jsonify(registeredUser.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# @auth_routes.route('/login', methods=['POST'])
# def login():
#     email = request.json.get('email')
#     password = request.json.get('password')

#     user = AuthService.authenticate(email, password)
#     if not user:
#         return jsonify({'message': 'Invalid credentials'}), 401

#     token = AuthService.generate_token(user)

#     return jsonify({'token': token.decode('UTF-8')})
