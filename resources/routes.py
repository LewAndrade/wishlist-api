from os import environ

from flask_restful import Api


from .wish import WishListApi, WishApi, RandomWishApi

API_URL = '/api/v1'


def initialize_routes(api: Api):
    api.add_resource(WishListApi, API_URL + '/wishlist')
    api.add_resource(WishApi, API_URL + '/wishlist/<wish_id>')
    api.add_resource(RandomWishApi, API_URL + '/wishlist/random')
