import pytest

from api.models import Post


@pytest.mark.django_db
class TestModels:
    title = "Test title",
    url = "test.com",
    news_id = 999999

    def test_post_save(self):
        post = Post.objects.create(
            title=self.title,
            url=self.url,
            news_id=self.news_id
        )
        assert post.title == self.title
        assert post.url == self.url
        assert post.news_id == self.news_id
