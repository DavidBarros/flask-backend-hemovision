from flask_pymongo import ObjetctId


class User:

    def __init__(self, _id, firstName, lastName, birthDate, email, password):
        self._id = id
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.email = email
        self.passowrd = password

    @staticmethod
    def from_dict(user_dict):
        return User(
            id=user_dict.get('_id', None),
            email=user_dict.get('email', None),
            password=user_dict.get('password', None)
        )

    def to_dict(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }
