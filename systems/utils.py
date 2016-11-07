import csv
from .models import System

class SystemsFile(object):
    mapping = {
        'name': 'name',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'eddb_id': 'id',
        # 'slug': 'name',
    }
    def __init__(self, file):
        self.file = csv.reader(file.splitlines(), delimiter=',')
        self.column = dict()

        index = 0
        row = self.file.next()
        for c in row:
            self.column[c] = index
            index += 1

    def save_obj(self, obj):
        try:
            entry = System.objects.get(eddb_id=obj['eddb_id'])
            System.objects.filter(eddb_id=obj['eddb_id']).update(**obj)
        except System.DoesNotExist:
            entry = System.objects.create(**obj)
        entry.save()

    def create_obj(self, row):
        obj = dict()
        for field in self.mapping:
            f = self.mapping[field]
            if f in self.column:
                obj[field] = row[self.column[f]]

        self.save_obj(obj)

    def import_file(self, limit=False):
        count = 0
        use_limit = False
        if limit or limit >= 0:
            use_limit = True

        for row in self.file:
            if use_limit and count >= limit:
                break;
            self.create_obj(row)
            count += 1


