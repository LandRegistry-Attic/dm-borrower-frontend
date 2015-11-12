from flask import Flask  # type: ignore
from flask import current_app, redirect
from flask.ext.script import Manager
from application.service.deed_api import make_deed_api_client
from .health.views import health
from .deed.searchdeed.views import searchdeed


def create_manager(deed_api_client=make_deed_api_client()):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.url_map.strict_slashes = False

    setattr(searchdeed, 'deed_api_client', deed_api_client)

    app.register_blueprint(health, url_prefix='/health')
    app.register_blueprint(searchdeed, url_prefix='/searchdeed')

    return manager
