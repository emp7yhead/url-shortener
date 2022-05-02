"""Config file for app."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Config variables."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
    ) or 'sqlite:///' + os.path.join(  # noqa: WPS336
        basedir,
        'urls.db',
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Config variables for production."""

    DEBUG = False


class StagingConfig(Config):
    """Config variables for staging."""

    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Config variables for development."""

    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Config variables for testing."""

    TESTING = True


CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    'default': DevelopmentConfig,
}
