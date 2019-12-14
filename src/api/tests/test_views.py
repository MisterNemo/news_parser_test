import json
import pytest

from django.urls import reverse
from rest_framework.test import APIRequestFactory

from api.views import PostViewSet
from api.models import Post


@pytest.fixture
def factory():
    return APIRequestFactory()


def test_post_list(factory, db):
    request = factory.get('/api/v1/posts/')
    post_view = PostViewSet.as_view(
        actions={
            'get': 'list',
        }
    )
    response = post_view(request)

    assert response.status_code == 200

