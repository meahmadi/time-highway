from mongoengine import Document, StringField,\
    DateTimeField, EmailField
import datetime


class UserModel(Document):
    firstname = StringField(max_length=50)
    lastname = StringField(max_length=50)
    email = EmailField(max_length=100, required=True, unique=True)
    password = StringField(min_length=1, max_length=200, required=True)
    signup_date = DateTimeField(default=datetime.datetime.utcnow)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
