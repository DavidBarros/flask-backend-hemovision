from flask import Flask

from .extensions import database
from .routes.authRoutes import authRoutes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(authRoutes)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/hemovision-db"
    database.init_app(app)

    return app

