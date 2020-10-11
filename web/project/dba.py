from project.models import User, Pace
from project import db
from project.schemas import PaceSchema

def get_values(sort="average_pace"):
    schema = PaceSchema()
    paces = Pace.query.all()
    result = [schema.dump(pace) for pace in paces]
    return result
