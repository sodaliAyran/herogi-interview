import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    env = os.getenv("FLASK_ENV")
    if  env == "production":
        DEBUG = False
        TESTING = False
    else:
        DEBUG=True
        TESTING=True
        DEVELOPMENT=True
    CSRF_ENABLED = True
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True



class TestingConfig(Config):
    TESTING = True
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
