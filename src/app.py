import logging

from flask import Flask
from flask_restful import Api

from admin import init_admin
from database import init_db
from apis import test_api


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object("config.Config")
init_db(app)

init_admin(app)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


api = Api(app)
api.add_resource(test_api.TestAPI, "/test")

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
