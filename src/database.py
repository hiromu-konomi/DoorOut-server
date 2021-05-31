from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


def init_db(app):
    ma.init_app(app)
    db.init_app(app)
    Migrate(app, db)
