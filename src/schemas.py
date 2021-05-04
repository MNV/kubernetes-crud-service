from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from src.models import UserModel

db = SQLAlchemy()


class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = UserModel
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
