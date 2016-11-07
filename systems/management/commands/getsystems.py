import csv
import requests

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from systems.utils import SystemsFile

class Command(BaseCommand):
    help = 'Imports Systems'

    def add_arguments(self, parser):
        parser.add_argument('limit', nargs='+')


    def handle(self, *args, **options):
        systems_csv = settings.EDDB_SYTEMS_FULL
        file = requests.get(systems_csv, verify=False).content.decode('utf-8')

        use_limit = False
        if 'limit' in options:
            try:
                limit = int(options['limit'][0])
                use_limit = True
                if limit < 0:
                    raise CommandError('Wrong argument for limit.')
            except ValueError:
                if options['limit'][0] != 'all':
                    raise CommandError('Wrong argument for limit.')

        f = SystemsFile(file)
        if use_limit:
            f.import_file(limit=limit)
        else:
            f.import_file()
