from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from database import db
from models import (
    User,
    Post,
    Comment,
    PostImagePath,
    Like,
    PostCoordinate,
    Tag,
    ExcludedCoordinate
)

admin = Admin()


def init_admin(app: Flask):
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Comment, db.session))
    admin.add_view(ModelView(PostImagePath, db.session))
    admin.add_view(ModelView(Like, db.session))
    admin.add_view(ModelView(PostCoordinate, db.session))
    admin.add_view(ModelView(Tag, db.session))
    admin.add_view(ModelView(ExcludedCoordinate, db.session))
