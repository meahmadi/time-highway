from flask import Flask, jsonify, abort, g
from flask.ext.restful import Api, reqparse
from flask.ext.login import LoginManager, login_user, logout_user,\
        login_required, current_user
from flask_cors import cross_origin
from mongoengine import *

from settings import *
from utils import url
from models import UserModel
from validation import auth_parser
from resources import EventResource, StoryResource, UserStoriesResource


app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

api = Api(app)
api.decorators = [login_required, cross_origin(headers=['Content-Type'])]

connect('timehighway', host=MONGO_HOST, port=MONGO_PORT,
        username=MONGO_USERNAME, password=MONGO_PASSWORD)

api.add_resource(EventResource, url('/event'))
api.add_resource(StoryResource, url('/story'))
api.add_resource(UserStoriesResource, url('/user/stories'))



@login_manager.user_loader
def user_loader(uid):
    return UserModel.objects(pk=uid).first()

@app.before_request
def global_user():
    g.user = current_user._get_current_object()

@app.route(url('/test'), methods=['GET', 'POST'])
def test():
    return jsonify({'response': 'Yaay, it works!'})

@app.route(url('/users/signup'), methods=['POST'])
@cross_origin(headers=['Content-Type'])
def signup():
    args = auth_parser.parse_args()
    u = UserModel.objects(email=args['email']).first()
    success = True
    err = ''
    data = {}
    if not u:
        if len(args['password']) == 0:
            return jsonify({'err': 'Password too short.'}), 400
        try:
            pass_hash = pwd_context.encrypt(args['password'])
            u = UserModel(email=args['email'], password=pass_hash).save()

        except ValidationError as e:
            err = ''
            if e.errors.keys():
                field = e.errors.keys()[0]
                err = '%s: %s' % (field, e.errors[field].message)
            return jsonify({'err': err}), 400

        login_user(u)

    else:
        success = False
        err = 'Email already exists.'

    return jsonify({
        'success': success,
        'err': err,
    })


@app.route(url('/users/login'), methods=['POST'])
@cross_origin(headers=['Content-Type'])
def login():
    args = auth_parser.parse_args()
    user = UserModel.objects(email=args['email']).first()
    if user:
        success = True
        err = ''
        data = {}
        if pwd_context.verify(args['password'], user.password):
            login_user(user)
            data = {
                'profile': {}
            }
        else:
            success = False
            err = 'Password is wrong.'
        return jsonify({
            'success': success,
            'err': err,
            'data': data,
        })
    else:
        return jsonify({'err': 'User doesn\'t exist.'}), 404

@app.route(url('/users/logout'), methods=['POST'])
@login_required
def logout():
    logout_user()
    return ''

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'err': 'Page not found.'}), 404

@app.errorhandler(400)
def page_not_found(e):
    return jsonify({'err': 'Bad request.'}), 400

@app.errorhandler(401)
def page_not_found(e):
    return jsonify({'err': 'Permission denied.'}), 401

@app.errorhandler(500)
def page_not_found(e):
    return jsonify({'err': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run()
