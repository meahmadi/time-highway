from mongoengine import Document,EmbeddedDocument, StringField,\
    DateTimeField, EmailField, ListField, ReferenceField, BooleanField,\
    EmbeddedDocumentField, FloatField, IntField, GenericReferenceField
import datetime


class UserModel(Document):
    firstname = StringField(max_length=50)
    lastname = StringField(max_length=50)
    email = EmailField(max_length=100, required=True, unique=True)
    password = StringField(min_length=1, max_length=200, required=True)
    signup_date = DateTimeField(default=datetime.datetime.utcnow)
    stories = ListField(ReferenceField('StoryModel')) # Root story

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class GroupModel(Document):
    owner = ReferenceField(UserModel, required=True)
    members = ListField(ReferenceField(UserModel))


class PermissionModel(EmbeddedDocument):
    group = ReferenceField(GroupModel, required=True)
    read_access = BooleanField(required=True, default=True)
    write_access = BooleanField(required=True, default=True)
    edit = BooleanField(required=True, default=False)
    delete = BooleanField(required=True, default=False)


class TModel(EmbeddedDocument):
    val = StringField()
    type = StringField() 
    gran = IntField(default=1000)
    prob = FloatField(min_value=0, max_value=1)


class DTModel(EmbeddedDocument):
    value = StringField()


class EventDataModel(EmbeddedDocument):
    what = StringField()
    

class EventModel(Document):
    parent = ReferenceField('EventModel', required=False)
    source = DateTimeField(default=datetime.datetime.utcnow) # Issue #2
    data = EmbeddedDocumentField(EventDataModel)
    t = EmbeddedDocumentField(TModel)
    dt = EmbeddedDocumentField(DTModel)
    tags = ListField(StringField(max_length=50))
    types = ListField(StringField(max_length=50))
    
    # By defualt must inherit from storyModel.permissions
    permissions = ListField(
        EmbeddedDocumentField(PermissionModel)
    ) 


class StoryModel(Document):
    name = StringField(max_length=100, required=True)
    description = StringField()
    items = ListField(ReferenceField('EventModel'))
    # owner = ReferenceField(UserModel, required=True)
    # sub_storys = ListField(ReferenceField('storyModel'))
    # events = ListField(ReferenceField(EventModel))
    permissions = ListField(
        EmbeddedDocumentField(PermissionModel)
    )
