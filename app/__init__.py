"""App initialization."""
from config import CONFIG
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name: str):
    """Create application.

    Args:
        config_name: config_name to create app with.

    Returns:
        app.
    """
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    db.init_app(app)

    with app.app_context():
        db.create_all()

        from app.views import url_shortener
        app.register_blueprint(url_shortener)

        return app
