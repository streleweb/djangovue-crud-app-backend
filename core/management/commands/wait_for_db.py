"""Django command - wait for db to be available."""
import time
from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django-Command to wait for db"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')
        db_up = False

        while db_up is False:
            try:
                # check if DB state is ready
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write('DB unavailable, waiting 1 more second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is now available.'))
