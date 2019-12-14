from django.core.management.base import BaseCommand

from api.utils import news_parse


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        news_parse()