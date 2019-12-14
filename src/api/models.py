from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=256
    )
    url = models.CharField(
        max_length=256
    )
    news_id = models.IntegerField()
    created = models.DateTimeField(
        auto_now_add=True
    )