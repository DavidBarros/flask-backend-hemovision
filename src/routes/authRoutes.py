from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_smorest import Blueprint, abort
from werkzeug.security import check_password_hash

from ..extensions.database import mongo
from ..extensions.schemas import LoginSchema

blp = Blueprint("Auth", "auth", description="Operations on auths")


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, authData):
        user = mongo.db.users.find_one({"email": authData["email"]})

        if user and check_password_hash(user["password"], authData["password"]):
            print(user)
            access_token = create_access_token(identity=user["_id"], fresh=True)
            refresh_token = create_refresh_token(user["_id"])
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")
