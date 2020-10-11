from project.models import User, Pace
from project import db
from project.schemas import PaceSchema

def get_values():

    schema = PaceSchema()
    paces = Pace.query.all()
    data = [schema.dump(pace) for pace in paces ]
    
    return data
