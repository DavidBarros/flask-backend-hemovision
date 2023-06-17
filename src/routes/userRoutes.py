from flask.views import MethodView
from flask_smorest import Blueprint, abort
from werkzeug.security import generate_password_hash

from ..extensions.database import mongo
from ..extensions.schemas import UserSchema
from ..models.user import User

blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, userData):
        if mongo.db.users.find_one(userData["email"]):
            abort(409, message="A user with that email already exists.")

        user = User(
            firstName=userData["firstName"],
            lastName=userData["lastName"],
            birthDate=userData["birthDate"],
            email=userData["email"],
            password=generate_password_hash(userData["password"]),
        )
        userDict = user.to_dict()
        mongo.db.users.insert_one(userDict)
        return {"message": "User created successfully."}, 201
