from project.models import User, Pace

def create_db(db):
    db.drop_all()
    db.create_all()
    db.session.commit()

def seed_db(db):
    with open("data/users.csv", "r") as f:
        for line in f.readlines():
            id, username, age, gender = line.strip().split(",")
            db.session.add(User(id=id, username=username, age=age,
            gender=gender))
    db.session.commit()
    with open("data/pace.csv", "r") as f:
        for line in f.readlines():
            user_id, total_time, distance = line.strip().split(",")
            db.session.add(Pace(user_id=user_id, total_time=total_time,
            distance=distance))
    db.session.commit()
