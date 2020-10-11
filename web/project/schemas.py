from project import ma
from project.models import User, Pace


def calculate_age_group(age):
    if age >= 20 and age < 30:
        age_group = "group1"
    elif age >= 30 and age < 40:
        age_group = "group2"
    elif age >= 40 and age < 60:
        age_group = "group3"
    else:
        age_group = "no_group"
    return age_group

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field()
    age = ma.auto_field()
    gender = ma.auto_field()
    age_group = ma.Function(lambda obj: calculate_age_group(int(obj.age)))


class PaceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pace

    total_time = ma.auto_field()
    distance = ma.auto_field()
    average_pace = ma.Function(lambda obj: \
     int(obj.total_time) / (int(obj.distance) / 1000))
    username = ma.Function(lambda obj: obj.user.username)
    age = ma.Function(lambda obj: obj.user.age)
    gender = ma.Function(lambda obj: obj.user.gender)
    age_group = ma.Function(lambda obj: calculate_age_group(int(obj.user.age)))
