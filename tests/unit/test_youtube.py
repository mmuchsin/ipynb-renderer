import pytest
from ipynb_renderer import get_time
from ipynb_renderer import InvalidURLException


good_url = [
    ("https://youtu.be/roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", 42),
]

bad_url = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
    ("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s")
]


@pytest.mark.parametrize("url, response", good_url)
def test_get_time_success(url, response):
    assert get_time(url) == response


@pytest.mark.parametrize("url", bad_url)
def test_get_time_failed(url):
    with pytest.raises(InvalidURLException):
        get_time(url)
