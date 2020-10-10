from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config.from_object("project.config.TestingConfig")
    else:
        app.config.from_object("project.config.Config")

    with app.app_context():
        from project.dba import create_db, seed_db
        from .views import api
        from .views import errors

        db.init_app(app)
        create_db(db)
        seed_db(db)

        app.register_blueprint(api.api_bp)
        app.register_blueprint(errors.error_bp)

    return app
