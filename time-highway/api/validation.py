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