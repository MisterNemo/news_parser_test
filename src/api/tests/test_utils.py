import requests


def test_url_request():
    URL = "https://news.ycombinator.com/"
    request = requests.get(url=URL + 'newest')

    assert request.status_code == requests.codes.ok
