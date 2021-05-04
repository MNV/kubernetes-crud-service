from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(20))

    def __init__(self, username, firstName, lastName, email, phone):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone

    def __repr__(self):

        return f"{self.username} ({self.firstName} {self.lastName})"

    def create(self):
        db.session.add(self)
        db.session.commit()

        return self
