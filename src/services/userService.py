from werkzeug.security import generate_password_hash

from ..extensions.database import mongo
from ..model.user import User


class userService:

    @staticmethod        
    def createUser(firstName, lastName, birthDate, email, password):
        newUser = User(firstName, lastName,
                       birthDate, email, generate_password_hash(password))
        mongo.db.users.insert_one(newUser.to_dict())
        return (newUser.to_dict())

    # def updateUser():
            

    # def deleteUser():