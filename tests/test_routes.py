"""Tests for routes."""
import pytest
from tests.fixtures import TEST_CONFIG, flask_app, client


@pytest.mark.parametrize('test_page, test_code', TEST_CONFIG)
def test_get(client, test_page, test_code):
    """Tests pages that the response to GET is valid.

    Args:
        client: Flask application configured for testing.
        test_page: tested page.
        test_code: expected response code.
    """
    response = client.get(test_page)
    assert response.status_code == 200
    assert b'UrlShortener' in response.data


@pytest.mark.parametrize('test_page, test_code', TEST_CONFIG)
def test_post(client, test_page, test_code):
    """Tests pages that the response returns correct status code.

    Args:
        client: Flask application configured for testing.
        test_page: tested page.
        test_code: expected response code.
    """
    response = client.post(test_page)
    assert response.status_code == test_code
    assert b'UrlShortener' not in response.data


def test_page_not_found(client):
    """Tests pages that the response to non-existent path returns 404.

    Args:
        client: Flask application configured for testing.
    """
    response = client.get('/hello/post')
    assert response.status_code == 404


def test_post_url(client):
    """Test page that the form data was send successfullys.

    Args:
        client: Flask application configured for testing.
    """
    with client:
        response = client.post('/', data={'url': 'http://test.com'})
        assert response.status_code == 200
