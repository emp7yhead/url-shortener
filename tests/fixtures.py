"""Fixtures for testing."""
import pytest
from app import create_app

TEST_CONFIG = [
    ('/', 400),
    ('/stats/page/1', 405),
    ('/about', 405),
]


@pytest.fixture()
def flask_app():
    """Fixture for created app.

    Yields:
        app.
    """
    app = create_app('testing')
    yield app


@pytest.fixture()
def client(flask_app):
    """Create test client.

    Args:
        flask_app: Flask application configured for testing.

    Returns:
        app.
    """
    return flask_app.test_client()
