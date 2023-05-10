from pymongo import MongoClient
from ..models.user import User


client = MongoClient('mongodb://localhost:27017/')
db = client['hemovision-db']
collection = db['users']


class AuthService:

    def createUser(firstName, lastName, birthDate, email, password):
        newUser = User(firstName=firstName, lastName=lastName,
                       birthDate=birthDate, email=email, password=password)
        db.users.insert_one(newUser.to_dict())
        return (newUser.to_dict())

    # def authenticate():

    # def generate_token():
