class User:

    def __init__(self,  firstName: str, lastName: str,
                 birthDate: str, email: str, password: str):
        self._id = None
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.email = email
        self.password = password

    @staticmethod
    def from_dict(user_dict):
        return User(

            firstName=user_dict.get('firstName'),
            lastName=user_dict.get('lastName'),
            birthDate=user_dict.get('birthDate'),
            email=user_dict.get('email'),
            password=user_dict.get('password')
        )

    def to_dict(self):
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'birthDate': self.birthDate,
            'email': self.email,
            'password': self.password
        }
