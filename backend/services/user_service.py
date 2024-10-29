from ..models.user_model import User
from ..requests.user_create_request import UserCreationRequest
from .. import db

def create_user(request: UserCreationRequest):
    user = User(name=request.name, surname=request.surname, birth_year=request.birth_year, 
                gender=request.gender, school_grade=request.school_grade, email=request.email,
                password=request.password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()