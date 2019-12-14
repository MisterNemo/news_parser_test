from django.conf.urls import url

from rest_framework import routers

from api.views import PostViewSet

router = routers.SimpleRouter()

router.register(
    r'posts',
    PostViewSet,
    base_name='posts'
)

api_urlpatterns = [
]

api_urlpatterns += router.urls
