from flask import Flask  # type: ignore
from flask.ext.script import Manager
from application.service.deed_api import make_deed_api_client
from .health.views import health
from .deed.searchdeed.views import searchdeed
from .borrower.views import borrower_landing
import os
import logging
from logger import logging_config


logging_config.setup_logging()
LOGGER = logging.getLogger(__name__)

LOGGER.info("Starting the server")


def create_manager(deed_api_client=make_deed_api_client()):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    manager = Manager(app)
    app.url_map.strict_slashes = False

    setattr(searchdeed, 'deed_api_client', deed_api_client)
    setattr(borrower_landing, 'deed_api_client', deed_api_client)

    app.register_blueprint(health, url_prefix='/health')
    app.register_blueprint(searchdeed)
    app.register_blueprint(borrower_landing)

    app.secret_key = os.urandom(32)

    return manager
