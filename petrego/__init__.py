import os

from flask import Flask
from . import db, help
from .apiv1 import APIV1
from .apiv2 import APIV2
from .jsonformatter import JSONFormatter
from .sqlitehelper import SQLiteHelper

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'petrego.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize the database
    db.init_app(app)

    # register blueprints
    app.register_blueprint(APIV1(SQLiteHelper(), JSONFormatter(),
        'apiv1', __name__))
    app.register_blueprint(APIV2(SQLiteHelper(), JSONFormatter(),
        'apiv2', __name__))
    app.register_blueprint(help.bp)

    return app
