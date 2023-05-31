# from flask import Flask, jsonify, request
# from flask import PyMongo
# from flask import jwt
# from datetime import datetime, timedelta
# from functools import wraps

# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
# app.config["SECRET_KEY"] = "mysecretkey"
# mongo = PyMongo(app)


# @app.route("/login", methods=["POST"])
# def login():
#     email = request.json.get("email", None)
#     password = request.json.get("password", None)
#     user = mongo.db.users.find_one({"email": email})
#     if not user:
#         return jsonify({"message": "Invalid credentials"}), 401
#     if password != user["password"]:
#         return jsonify({"message": "Invalid credentials"}), 401
#     token = jwt.encode(
#         {"user_id": str(user["_id"]),
#          "exp": datetime.utcnow() + timedelta(minutes=30)},
#         app.config["SECRET_KEY"],
#     )
#     return jsonify({"token": token.decode("UTF-8")})


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get("Authorization", None)
#         if not token:
#             return jsonify({"message": "Token is missing"}), 401
#         try:
#             data = jwt.decode(
#                 token, app.config["SECRET_KEY"], algorithms=["HS256"])
#         except:
#             return jsonify({"message": "Token is invalid"}), 401
#         return f(*args, **kwargs)

#     return decorated


# app.run(debug=True)
