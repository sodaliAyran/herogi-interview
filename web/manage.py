from flask.cli import FlaskGroup
from project import app, db
from project.models import User, Pace

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
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

if __name__ == "__main__":
    cli()
