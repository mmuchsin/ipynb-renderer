import pytest
from ipynb_renderer import render_youtube
from ipynb_renderer import InvalidURLException


class TestYouTubeVideoRenderer:
    good_url = [
        ("https://youtu.be/roO5VGxOw2s", "success"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s", "success"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", "success"),
    ]

    bad_url = [
        ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),
        ("https://www.youtube.com/watch?v=roO5VGxOw00"),
        ("https://www.youtube.com/watch?v=roO5VGxOw__"),
        ("https://www.youtube.com/watch?v=roO5VGxOwpp"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),
        ("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s"),
    ]

    @pytest.mark.parametrize("URL, response", good_url)
    def test_render_youtube_success(self, URL, response):
        assert render_youtube(URL) == response

    @pytest.mark.parametrize("URL", bad_url)
    def test_render_youtube_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_youtube(URL)
