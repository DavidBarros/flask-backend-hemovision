from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from .config import Config
from .extensions import database
from .routes.authRoutes import blp as AuthBlueprint
from .routes.userRoutes import blp as UserBlueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    database.init_app(app)
    JWTManager(app)

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(AuthBlueprint)

    return app
