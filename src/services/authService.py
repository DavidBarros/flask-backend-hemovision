from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from ..extensions.database import mongo



class AuthService:
    @staticmethod
    def authenticateUser(email, password):
        user = mongo.db.users.find_one({"email": email})
        if user and check_password_hash(user['password'], password):
            return user
        return None

    @staticmethod
    def generateToken(user_id):
        access_token = create_access_token(identity=user_id)
        return {"access_token": access_token}
        
        
