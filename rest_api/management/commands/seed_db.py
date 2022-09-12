from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        print('Populating the database...')
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'seed.sql')
        sql = Path(file_path).read_text()

        set_mod = os.environ.get('DJANGO_SETTINGS_MODULE')
        with connection.cursor() as cursor:
            if set_mod is None:
                cursor.executescript(sql)
            else:
                cursor.execute(sql)
