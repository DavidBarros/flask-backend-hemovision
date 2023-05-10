class User:

    def __init__(self,  firstName, lastName, birthDate, email, password):
        self._id = None
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.email = email
        self.password = password

    @staticmethod
    def from_dict(user_dict):
        return User(
            _id=user_dict.get('_id'),
            firstName=user_dict.get('firstName'),
            lastName=user_dict.get('lastName'),
            birthDate=user_dict.get('birthDate'),
            email=user_dict.get('email'),
            password=user_dict.get('password')
        )

    def to_dict(self):
        return {
            '_id': self._id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'birthDate': self.birthDate,
            'email': self.email,
            'password': self.password
        }
