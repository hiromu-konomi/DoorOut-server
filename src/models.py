import datetime
import uuid

from sqlalchemy.orm import backref
from sqlalchemy_utils import UUIDType

from database import db


# 投稿とタグの関係テーブル
posts_tags_table = db.Table(
    'posts_tags',
    db.Column('post_id', UUIDType(binary=False),
              db.ForeignKey('posts.post_id')),
    db.Column('tag_id', UUIDType(binary=False),
              db.ForeignKey('tags.tag_id'))
)

# ユーザーとフォロワーの関係デーブル
followers_table = db.Table(
    'followers',
    db.Column('follower_id', UUIDType(binary=False),
              db.ForeignKey('users.user_id')),
    db.Column('followed_id', UUIDType(binary=False),
              db.ForeignKey('users.user_id'))
)


class User(db.Model):
    """
    ユーザーのモデルクラス
    """
    __tablename__ = "users"

    user_id = db.Column(UUIDType(binary=False),
                        primary_key=True, default=uuid.uuid4)
    # TODO: account_idのlenを決める
    account_id = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    # TODO: account_idのlenを決める
    password = db.Column(db.String(255), nullable=False)
    user_image_path = db.Column(db.String(255), nullable=True)
    posts = db.relationship("Post", backref='user', lazy=True)
    likes = db.relationship("Like", backref='user', lazy=True)
    excluded_coordinates = db.relationship(
        "ExcludedCoordinate", backref='user', lazy=True)
    followed = db.relationship(
        "User", secondary=followers_table,
        primaryjoin=(followers_table.c.followed_id == user_id),
        secondaryjoin=(followers_table.c.follower_id == user_id),
        backref=db.backref('followers', lazy=True), lazy=True)
    version = db.Column(db.Integer, nullable=False, default=0)
    last_login_date = db.Column(db.DateTime, nullable=False,
                                default=datetime.datetime.now)
    create_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.now)


class Post(db.Model):
    """
    投稿のmodel
    """
    __tablename__ = "posts"

    post_id = db.Column(UUIDType(binary=False),
                        primary_key=True, default=uuid.uuid4)
    # user = db.relationship("User", backref='user', lazy=True)
    user_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("users.user_id"),
                        nullable=False)
    post_image_paths = db.relationship("PostImagePath")
    # TODO: 記事の内容の文字数を決める
    content = db.Column(db.String(255), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.now,
                           onupdate=datetime.datetime.now)
    post_type = db.Column(db.String(1), nullable=False)
    post_coordinates = db.relationship(
        "PostCoordinate", backref="post", lazy=True)
    likes = db.relationship("Like", backref="post", lazy=True)
    comments = db.relationship("Comment", backref="post", lazy=True)
    # temporary:0 投稿済:1 deleted:9
    status = db.Column(db.String(1), nullable=False, default="0")
    tags = db.relationship(
        "Tag", secondary=posts_tags_table, back_populates="posts")
    place_name = db.Column(db.String(255), nullable=False)
    comment_counts = db.Column(db.Integer, nullable=False, default=0)
    like_counts = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.String(1), nullable=False, default="0")  # deleted:9
    version = db.Column(db.Integer, nullable=False, default=0)


class PostImagePath(db.Model):
    __tablename__ = "post_image_paths"

    post_image_path_id = db.Column(UUIDType(binary=False),
                                   primary_key=True, default=uuid.uuid4)

    post_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("posts.post_id"))

    post_image_path = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(1), nullable=False, default="0")  # deleted:9


class Like(db.Model):
    __tablename__ = "likes"

    like_id = db.Column(UUIDType(binary=False),
                        primary_key=True, default=uuid.uuid4)
    post_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("posts.post_id"),
                        nullable=False)
    # いいねしたユーザー
    user_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("users.user_id"),
                        nullable=False)
    create_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.now)
    status = db.Column(db.String(1), nullable=False, default="0")  # deleted:9


class PostCoordinate(db.Model):
    __tablename__ = "post_coordinates"

    coordinate_id = db.Column(UUIDType(binary=False),
                              primary_key=True, default=uuid.uuid4)
    post_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("posts.post_id"),
                        nullable=False)
    # TODO: 緯度経度の桁数を確認し反映させる
    latitude = db.Column(db.String(10), nullable=False)
    longitude = db.Column(db.String(10), nullable=False)
    # 経路の登録座標の順番
    load_index = db.Column(db.String(255))
    status = db.Column(db.String(1), nullable=False, default="0")  # deleted:9


class Comment(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(UUIDType(binary=False),
                           primary_key=True, default=uuid.uuid4)
    post_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("posts.post_id"),
                        nullable=False)
    parent_comment_id = db.Column(
        UUIDType(binary=False), db.ForeignKey('comments.comment_id'))
    content = db.Column(db.String(255), nullable=False)
    child_comments = db.relationship(
        "Comment", backref=backref('parent'), remote_side=[comment_id])
    status = db.Column(db.String(1), nullable=False, default="0")  # deleted:9
    create_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.now)


class Tag(db.Model):
    __tablename__ = "tags"

    tag_id = db.Column(UUIDType(binary=False),
                       primary_key=True, default=uuid.uuid4)
    tag_name = db.Column(db.String(255), nullable=False)
    posts = db.relationship(
        "Post", secondary=posts_tags_table, back_populates="tags")
    status = db.Column(db.String(1), nullable=False, default="0")  # deleted:9


class ExcludedCoordinate(db.Model):
    __tablename__ = "excluded_coordinates"

    excluded_coordinate_id = db.Column(UUIDType(binary=False),
                                       primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUIDType(binary=False),
                        db.ForeignKey("users.user_id"),
                        nullable=False)
    latitude = db.Column(db.String(10), nullable=False)
    longitude = db.Column(db.String(10), nullable=False)
    place_name = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(1), nullable=False, default="0")  # deleted:9
