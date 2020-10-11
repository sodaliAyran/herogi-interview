from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()

def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config.from_object("project.config.TestingConfig")
    else:
        app.config.from_object("project.config.Config")

    with app.app_context():
        from .views import api
        from .views import errors
        from project.models import User, Pace

        db.init_app(app)
        ma.init_app(app)
        cors.init_app(app)

        db.drop_all()
        db.create_all()
        db.session.commit()

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

        app.register_blueprint(api.api_bp)
        app.register_blueprint(errors.error_bp)

    return app
