from marshmallow_sqlalchemy import fields

from database import ma
from models import Post, Tag, Comment


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
    tags = fields.Nested(TagSchema, many=True)
    comments = fields.Nested(CommentSchema, many=True)
