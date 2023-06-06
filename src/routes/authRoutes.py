from flask import Blueprint, jsonify, request

from ..services.authService import AuthService

authRoutes = Blueprint('auth_routes', __name__)


@authRoutes.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = AuthService.authenticateUser(email, password)
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    token = AuthService.generateToken(user['_id'])

    return token
