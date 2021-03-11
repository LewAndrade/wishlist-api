from random import choice

from flask import Response, request
from flask_restful import Resource

from database.models import Wish


class WishListApi(Resource):
    @staticmethod
    def get():
        wishlist = Wish.objects().to_json()
        return Response(wishlist, status=200, mimetype="application/json")

    @staticmethod
    def post():
        body = request.get_json()
        wish = Wish(**body).save()
        return {'id': str(wish.id)}, 200


class WishApi(Resource):
    @staticmethod
    def get(wish_id):
        wish = Wish.objects.get(id=wish_id).to_json()
        return Response(wish, mimetype="application/json", status=200)

    @staticmethod
    def put(wish_id):
        body = request.get_json()
        Wish.objects.get(id=wish_id).update(**body)
        return 'Wish updated', 200

    @staticmethod
    def delete(wish_id):
        Wish.objects.get(id=wish_id).delete()
        return 'Wish removed', 200


class RandomWishApi(Resource):
    @staticmethod
    def get():
        random_wish = choice(Wish.objects()).to_json()
        return Response(random_wish, mimetype="application/json", status=200)
