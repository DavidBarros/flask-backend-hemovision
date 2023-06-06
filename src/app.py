from flask import Flask


from .config import Config
from .extensions import database
from .routes.userRoutes import userRoutes
from .routes.authRoutes import authRoutes
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.register_blueprint(userRoutes)
    app.register_blueprint(authRoutes)
    app.config.from_object(Config)   
    database.init_app(app)
    JWTManager(app)

    return app






