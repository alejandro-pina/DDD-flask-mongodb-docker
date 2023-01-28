from flask import Flask, make_response, request
from flask_jwt_extended import JWTManager
from config import config
from .db import DB
ctx_db = DB()

def create_app(config_name):
    print(config[config_name])
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    ctx_db.init_app(app)
    JWTManager(app)

    @app.before_request
    def limit_methods():
        if request.method not in ['GET', 'POST', 'DELETE', 'PUT']:
            return make_response('',666)
            
    from app.api import api
    app.register_blueprint(api, url_prefix=app.config.get('API_PUBLIC', '/'))

    from app.auth import auth
    app.register_blueprint(auth, url_prefix=app.config.get('AUTH_PATH', '/'))

    @app.route('/', methods=('GET', 'POST'))
    def wellcome():
        return 'Wellcome to example DDD API 🛰'

    return app