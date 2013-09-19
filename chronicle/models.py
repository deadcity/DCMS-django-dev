from django.contrib.auth.models import User
from django.db import models

from common.metaclasses import Model_Metaclass


class Chronicle(models.Model):
    __metaclass__ = Model_Metaclass

    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 255, unique = True)

    storytellers = models.ManyToManyField(User, related_name = 'storyteller_for_chronicles')
    description = models.TextField(blank = True)

    def __unicode__ (self):
        return self.name if self.name and self.name is not '' else '<chronicle>'


class Game (models.Model):
    __metaclass__ = Model_Metaclass

    enabled = models.BooleanField(default = True)

    name      = models.CharField(max_length = 255, unique = True)
    chronicle = models.ForeignKey(Chronicle)
    date      = models.DateField()

    def __unicode__ (self):
        return '{}: {}'.format(self.chronicle.name, self.name)

    class Meta (object):
        ordering = ('chronicle', 'date',)
