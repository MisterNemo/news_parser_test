from rest_framework.response import Response
from rest_framework import viewsets,  mixins
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from api.serializer import PostSerializer

from api.models import Post

from api.pagination import PostLimitOffsetPagination


class PostViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):

    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    queryset = Post.objects.all().order_by('-id')
    pagination_class = PostLimitOffsetPagination
    serializer_classes = {
        'list': PostSerializer,
    }

