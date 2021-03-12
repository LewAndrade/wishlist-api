from json import dumps, loads
from random import choice

from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from database.models import Wish, User


class WishListApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        wishlist = dumps([loads(wish.to_json()) for wish in user.wishlist])
        print(wishlist)

        return Response(wishlist, status=200, mimetype="application/json")

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        wish = Wish(**body, added_by=user)
        wish.save()
        user.update(push__wishlist=wish)
        user.save()

        return {'id': str(wish.id)}, 200


class WishApi(Resource):
    @jwt_required()
    def get(self, wish_id):
        user_id = get_jwt_identity()
        wish = Wish.objects.get(id=wish_id, added_by=user_id).to_json()
        return Response(wish, mimetype="application/json", status=200)

    @jwt_required()
    def put(self, wish_id):
        user_id = get_jwt_identity()
        wish = Wish.objects.get(id=wish_id, added_by=user_id)
        body = request.get_json()
        wish.update(**body)
        return 'Wish updated', 200

    @jwt_required()
    def delete(self, wish_id):
        user_id = get_jwt_identity()
        wish = Wish.objects.get(id=wish_id, added_by=user_id)
        wish.delete()
        return 'Wish deleted', 200


class RandomWishApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        random_wish = dumps(choice([loads(wish.to_json()) for wish in user.wishlist]))
        return Response(random_wish, mimetype="application/json", status=200)
