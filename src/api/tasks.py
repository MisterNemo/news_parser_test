from __future__ import absolute_import, unicode_literals

from celery.task import periodic_task
from celery.schedules import crontab

from api.utils import news_parse


@periodic_task(run_every=(crontab(minute='*/5')), name="news_parse_task")
def news_parse_task():
    news_parse()
