from .. import db, flask_bcrypt
import datetime
from pytz import timezone as pytz_timezone


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10))
    school_grade = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now(tz=pytz_timezone('Turkey')))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now(tz=pytz_timezone('Turkey')), onupdate=datetime.datetime.now(tz=pytz_timezone('Turkey')))

    @password.setter
    def set_password(self, password):
        self.password = flask_bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User: {self.username}>"