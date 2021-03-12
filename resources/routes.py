from flask_restful import Api

from .auth import SignupApi, LoginApi
from .wish import WishListApi, WishApi, RandomWishApi

API_URL = '/api/v1'


def initialize_routes(api: Api):
    api.add_resource(WishListApi, API_URL + '/wishlist')
    api.add_resource(WishApi, API_URL + '/wishlist/<wish_id>')
    api.add_resource(RandomWishApi, API_URL + '/wishlist/random')

    api.add_resource(SignupApi, API_URL + '/auth/signup')
    api.add_resource(LoginApi, API_URL + '/auth/login')
