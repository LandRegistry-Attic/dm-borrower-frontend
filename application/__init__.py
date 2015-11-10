from flask import Flask  # type: ignore
from flask import render_template, current_app, redirect
from flask.ext.script import Manager
from application import helloworld, static
from application.service.deed_api import make_deed_client
from .helloworld.views import helloworld
from .deed.searchdeed.views import searchdeed


def create_manager(deed_api_client=make_deed_client):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    static.register_assets(app)

    app.register_blueprint(helloworld, url_prefix='/helloworld')
    app.register_blueprint(searchdeed, url_prefix='/searchdeed')

    @app.route('/')
    def index():
        # TODO: for now just redirect to the searchdeed landing page
        response = current_app.make_response(redirect('/searchdeed', code=303))
        return response

    return manager
