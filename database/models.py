from database import db


class Wish(db.Document):
    title = db.StringField(required=True)
    description = db.StringField()
    url = db.StringField()
    image = db.StringField()
