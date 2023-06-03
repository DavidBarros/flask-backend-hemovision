from flask import Flask

from .routes.authRoutes import auth_routes

app = Flask(__name__)

app.register_blueprint(auth_routes)


# if __name__ == '__main__':
#     app.run(debug=True)
