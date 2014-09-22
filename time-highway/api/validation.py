from flask import abort
from flask.ext.restful import reqparse
from validate_email import validate_email


def email_type(value):
    if value:
        try:
            value = str(value)
        except ValueError:
            abort(422)
        if value.strip():
            if validate_email(value):
                return value

    abort(422)


auth_parser = reqparse.RequestParser()
auth_parser.add_argument('email', type=email_type, required=True)
auth_parser.add_argument('password', type=unicode, required=True)

group_parser = reqparse.RequestParser()
# group_parser.add_argument('members', type=list, required=True)

user_parser = reqparse.RequestParser()

get_event_parser = reqparse.RequestParser()
get_event_parser.add_argument('event_id', type=str)

add_event_parser = reqparse.RequestParser()
add_event_parser.add_argument('parent', type=str, required=False)
add_event_parser.add_argument('source', type=str)
add_event_parser.add_argument('data', type=dict)
add_event_parser.add_argument('t', type=dict)
add_event_parser.add_argument('dt', type=dict)
add_event_parser.add_argument('types', type=str, action='append')
add_event_parser.add_argument('tags', type=str, action='append')
