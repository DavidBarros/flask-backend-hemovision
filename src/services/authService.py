from werkzeug.security import check_password_hash

from ..extensions.database import mongo


class AuthService:

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
