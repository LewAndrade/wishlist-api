from flask import Flask
from flask_restful import Api

from database import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('config.py')

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run()
