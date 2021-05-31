from flask_jwt_extended import (JWTManager, create_access_token,
                                create_refresh_token, get_jwt_claims,
                                get_jwt_identity, jwt_refresh_token_required,
                                jwt_required, set_access_cookies,
                                set_refresh_cookies, unset_jwt_cookies,
                                verify_jwt_in_request)
from flask_restful import Resource, reqparse
from sqlalchemy import or_

from database import db
from models import User, UserSchema

login_parser = reqparse.RequestParser()
login_parser.add_argument("email_or_account_id", type=str)
login_parser.add_argument("password", type=str)


def login():
    pass


def logout():
    pass


def register_user():
    pass


class ExecutedCoordinate():

    def post(self):
        pass

    def delete(self):
        pass


def update_user_password():
    pass


def update_user_profile():
    pass
