from werkzeug.security import check_password_hash, generate_password_hash

from ..extensions.database import mongo
from ..model.user import User


class AuthService:

    @staticmethod        
    def createUser(firstName, lastName, birthDate, email, password):
        newUser = User(firstName, lastName,
                       birthDate, email, generate_password_hash(password))
        mongo.db.users.insert_one(newUser.to_dict())
        return (newUser.to_dict())
    
    @staticmethod
    def authenticateUser(email, password):
        user = mongo.db.users.find(email)
        if user and check_password_hash(user.password, password):
            return user
        return None
    # def generate_token():

###
###
###
###
