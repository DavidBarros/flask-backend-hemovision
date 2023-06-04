from flask import Blueprint, jsonify, request

from ..services.authService import AuthService

authRoutes = Blueprint('auth_routes', __name__)






@authRoutes.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = AuthService.authenticate(email, password)
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    token = AuthService.generate_token(user)

    return jsonify({'token': token.decode('UTF-8')})
