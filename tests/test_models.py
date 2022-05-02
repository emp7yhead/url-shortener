from app.models import Url


def test_new_url():
    """
    GIVEN a Url model
    WHEN a new Url is created
    THEN check the original url, clicks count
    """
    test_url = Url(original_url='test.com')
    assert test_url.original_url == 'test.com'