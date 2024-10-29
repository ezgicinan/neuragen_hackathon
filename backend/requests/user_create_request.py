#backend/requests/user_create_request.py

class UserCreationRequest:
    def __init__(self, name, surname, birth_year, gender, school_grade, email, password):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.gender = gender
        self.school_grade = school_grade
        self.email = email
        self.password = password
