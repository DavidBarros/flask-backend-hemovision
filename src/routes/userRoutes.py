from flask import Blueprint, jsonify, request

from ..services.userService import userService

userRoutes = Blueprint("userRoutes", __name__)

@userRoutes.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        registeredUser = userService.createUser(firstName=data.get("firstName"), 
                                                lastName=data.get("lastName"), 
                                                birthDate=data.get("birthDate"), 
                                                email=data.get("email"), 
                                                password=data.get("password"))
        
        registeredUser["email"] = str(data.get("email"))

        return jsonify(f"{registeredUser['firstName']}, seu cadastro foi realizado com sucesso"), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400        