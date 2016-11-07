from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class System(models.Model):
    name = models.CharField(verbose_name='Name', max_length=140)
    x = models.FloatField(verbose_name='Coordinate X')
    y = models.FloatField(verbose_name='Coordinate Y')
    z = models.FloatField(verbose_name='Coordinate Z')
    eddb_id = models.IntegerField(unique=True)
    # slug = models.SlugField(verbose_name='Slug', unique=True)

    class Meta:
        verbose_name = "System"
        verbose_name_plural = "Systems"

    def __str__(self):
        return self.name

    # @models.permalink
    # def get_absolute_url(self):
    #     return self.slug
