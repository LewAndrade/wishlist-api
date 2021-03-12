from flask_bcrypt import generate_password_hash, check_password_hash

from database import db


class Wish(db.Document):
    title = db.StringField(required=True)
    description = db.StringField()
    url = db.StringField()
    image = db.StringField()
    added_by = db.ReferenceField('User')


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_lenght=6)
    wishlist = db.ListField(db.ReferenceField('Wish', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Wish, 'added_by', db.CASCADE)
