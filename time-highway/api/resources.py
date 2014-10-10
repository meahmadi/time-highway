import datetime

from flask import request, g
from flask.ext.restful import Resource, reqparse, fields, marshal_with, marshal
from flask.ext.restful.utils.cors import crossdomain
from flask.ext.login import login_required
from flask_cors import cross_origin
from mongoengine import ValidationError
from bson.objectid import ObjectId
from bson.errors import InvalidId

from models import UserModel, EventModel, StoryModel
from validation import auth_parser, get_event_parser, add_event_parser, story_parser

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
	'gran': fields.Float,
	'prob': fields.Float,
}

event_dt_fields = event_t_fields.copy()

event_fields = {
	'parent': fields.String,
	'source': DateTimeField,
	'data': fields.Nested(event_data_fields),
    'types': fields.List,
    'tags': fields.List,
    't': fields.Nested(event_t_fields),
    'dt': fields.Nested(event_dt_fields),
}


class StoryResource(Resource):

    def post(self):
        args = story_parser.parse_args()

        try:
            story = StoryModel.objects(pk=args['story_id']).first()
        except ValidationError:
            return {'err': 'Story not found.'}, 404

        # Basic permission implemention, must change
        if story not in g.user.stories:
            return {'err': 'You do not have access.'}, 403

        try:
            events = list()
            for e in args['events']:
                event = EventModel.objects(pk=e).first()
                events.append(event)
        
        except:
            return {'err': 'Event not found.'}, 404

        try:
            g.user.stories.append(events)
            g.user.save()

        except:
            return {'err': 'Error while saving.'}, 404 
        
        return {'successful': True}

    def get(self):
        pass


class UserStoriesResource(Resource):

    def get(self):
        data = []
        try:
            stories = g.user.stories
        except ValidationError:
            return {}, 404

        data = {
            'stories': [str(s.id) for s in stories],    
        }
        return {'data': data}

    def post(self):
        args = add_story_parser.parse_args()

        try:
            events = list()
            for e in args['events']:
                event = EventModel.objects(pk=e).first()
                events.append(event)
        except:
            return {'err': 'Event not found.'}, 404


        try:
            g.user.stories.append(events)
            g.user.save()

        except:
            return {'err': 'Error while saving.'}, 404

class EventResource(Resource):

	def post(self):
		args = add_event_parser.parse_args()

	# def get(self):
	# 	args = get_event_parser.parse_args()
 #        try:
 #            event = EventModel.objects(pk=args['event_id']).first()
 #        except ValidationError:
 #            return {}, 404

 #        if event:
 #        	data = marshal(event, event_fields)
 #        	return {'data': data}
 #        else:
 #            return {'err': 'Event not found.'}, 404

