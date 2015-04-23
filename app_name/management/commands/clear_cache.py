from django.core.management.base import BaseCommand
from django.core.cache import cache


class Command(BaseCommand):
    """
    Command to clear memcache.
    """
    help = "Clear cache"

    def handle(self, *args, **options):
        cache.clear()