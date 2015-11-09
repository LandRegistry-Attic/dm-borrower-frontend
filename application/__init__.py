from flask import Flask  # type: ignore
from flask import render_template
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

    # app.register_blueprint(searchdeed, url_prefix='/searchdeed')

    # app.register_blueprint(search.blueprint)
    # app.register_blueprint(view.blueprint(deed_api_client()))
    # app.register_blueprint(
    #     sign.blueprint(scribe_api_client(), deed_api_client())
    # )
    # app.register_blueprint(assets.govuk_template, url_prefix='/template')

    @app.route('/')
    def index():
        return render_template('home.html',
                               title='Home')

    return manager
