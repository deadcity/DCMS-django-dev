from django.db import models

from common.metaclasses import Model_Metaclass


class Chronicle(models.Model):
    __metaclass__ = Model_Metaclass

    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 256, unique = True)

    description = models.TextField(blank = True)


class Game(models.Model):
    __metaclass__ = Model_Metaclass

    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 256, unique = True)

    chronicle = models.ForeignKey(Chronicle)
    date = models.DateField()

    class Meta(object):
        ordering = ('chronicle', 'date',)
