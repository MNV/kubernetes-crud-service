import os

from flask import Flask, jsonify, request, make_response
from flask import json
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.config import Config
from src.models import UserModel
from src.schemas import UserSchema

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.errorhandler(Exception)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps(
        {
            "code": e.code,
            "message": e.description,
        }
    )
    response.content_type = "application/json"

    return response


@app.route("/health")
def health():
    return jsonify({"status": "OK"})


@app.route("/")
def index():
    return f"Hello from {os.environ['HOSTNAME']}!"


@app.route("/user", methods=["POST"])
def create():
    data = request.get_json()
    schema = UserSchema()
    user = schema.load(data)
    result = schema.dump(user.create())

    return make_response(jsonify(result), 200)


@app.route("/user/<user_id>", methods=["GET"])
def read(user_id: int):
    user_model = db.session.query(UserModel).get(user_id)
    schema = UserSchema()
    user = schema.dump(user_model)

    return make_response(jsonify(user))


@app.route("/user/<user_id>", methods=["PUT"])
def update(user_id: int):
    data = request.get_json()
    user_model = db.session.query(UserModel).get(user_id)
    if data.get("username"):
        user_model.username = data["username"]

    if data.get("firstName"):
        user_model.firstName = data["firstName"]

    if data.get("lastName"):
        user_model.lastName = data["lastName"]

    if data.get("email"):
        user_model.email = data["email"]

    if data.get("phone"):
        user_model.phone = data["phone"]

    db.session.commit()

    schema = UserSchema()
    user = schema.dump(user_model)

    return make_response(jsonify(user))


@app.route("/user/<user_id>", methods=["DELETE"])
def delete(user_id: int):
    user_model = db.session.query(UserModel).get(user_id)
    db.session.delete(user_model)
    db.session.commit()

    return make_response("", 204)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
