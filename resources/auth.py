import datetime

from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from database.models import User


class SignupApi(Resource):
    @staticmethod
    def post():
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        user_id = user.id
        return {'id': str(user_id)}, 201


class LoginApi(Resource):
    @staticmethod
    def post():
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error: invalid email or password'}, 401

        expires_at = datetime.timedelta(days=7)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires_at
        )
        return {'token': access_token}, 200
