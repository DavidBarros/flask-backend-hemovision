from flask import Blueprint, jsonify, request
from model.user import User
from services.auth_service import AuthService

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        firstName = data.get("firstName")
        lastName = data.get("lastName")
        birthDate = data.get("birthDate")
        email = data.get("email")
        password = data.get("password")

        registeredUser = AuthService.createUser(
            firstName, lastName, birthDate, email, password)
        registeredUser["email"] = str(email)

        return jsonify(f"{registeredUser['firstName']}, seu cadastro foi realizado com sucesso"), 201
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