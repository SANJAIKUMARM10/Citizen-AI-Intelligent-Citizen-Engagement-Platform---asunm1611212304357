from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from . import models

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY='dev-secret-key',
        SQLALCHEMY_DATABASE_URI='sqlite:///citizen_ai.sqlite3',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if config_object:
        app.config.from_object(config_object)

    db.init_app(app)
    migrate = Migrate(app, db)

    # register blueprints
    from .routes.main import bp as main_bp
    from .routes.api import bp as api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
