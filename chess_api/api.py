from flask import current_app, Flask, request, session
from . import distributor

def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(distributor.bp)
    app.before_request(before_request)

    return app

def before_request():
    return