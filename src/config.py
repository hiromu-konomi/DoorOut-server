import os


class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = \
        "mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(
            os.getenv('MYSQL_USER'),
            os.getenv('MYSQL_PASSWORD'),
            os.getenv('DATABASE_CONTAINER_NAME'),
            os.getenv('MYSQL_DATABASE'),
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = b'\x1e\x15\xbd\xcf[\x80\x17\xf4C;\x8a\xa1u\x96\x9a='


Config = DevelopmentConfig
