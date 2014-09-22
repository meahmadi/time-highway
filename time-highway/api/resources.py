import datetime

from flask import request, g
from flask.ext.restful import Resource, reqparse, fields, marshal_with, marshal
from flask.ext.restful.utils.cors import crossdomain
from flask.ext.login import login_required
from flask_cors import cross_origin
from mongoengine import ValidationError
from bson.objectid import ObjectId
from bson.errors import InvalidId

from models import UserModel, EventModel
from logger import logger
from validation import auth_parser

def format_datetime(value):
    return value.strftime('%Y-%m-%d %H:%M:%S.%f')

class DateTimeField(fields.Raw):

    def format(self, value):
        return format_datetime(value)

event_data_fields = {
	'what': fields.String,
}

event_t_fields = {
	'val': fields.String,
	'type': fields.String,
	'gran': fields.Int,
	'prob': fields.Float,
}

event_dt_fields = event_t_fields.copy()

event_fields = {
	'parent': fields.String,
	'source': DateTimeField,
	'data': fields.Nested(event_data_fields)
    'types': fields.List,
    'tags': fields.List,
    't': fields.Nested(event_t_fields),
    'dt': fields.Nested(event_dt_fields),
}

class EventModel(Resource):

	def post(self):
		pass

	def get(self):
		args = event_parser.parse_args()
        try:
            event = EventModel.objects(pk=args['event_id']).first()
        except ValidationError:
            return {}, 404

        if event:
        	data = marshal(event, event_fields)
        	return {'data': data}
		else:
            return {'err': 'Event not found.'}, 404

