from flask_restx import Resource, reqparse
from flask import jsonify
import polyline

from models import Post
from schemas import PostSchema


class TestAPI(Resource):
    """
    動作確認用のクラス
    TODO: 削除する
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(TestAPI, self).__init__()

    def get(self):
        results = Post.query.all()
        json_data = PostSchema(many=True).dump(results)
        print(results)
        return jsonify(json_data)

    def delete(self):
        endoded_route: str = polyline.encode(
            [(38.5, -120.2), (40.7, -120.9), (43.2, -126.4)], 5)
        return endoded_route
