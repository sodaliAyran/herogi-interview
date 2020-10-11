from project.models import User, Pace
from project import db
from project.schemas import UserSchema

def get_values(sort="average_pace"):
    user_schema = UserSchema()
    print(user_schema.dump(User.query.first()))
    return None
