from project import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(25), nullable=False)
    paces = db.relationship("Pace", backref="user", lazy=True)

    def __init__(self, username, age, gender, id=None):
        if id :
            self.id = id
        self.username = username
        self.age = age
        self.gender = gender

class Pace(db.Model):
    __tablename__ = "pace"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    total_time = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, total_time, distance):
        self.user_id = user_id
        self.total_time = total_time
        self.distance = distance
