from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import escape


class EnumModel (models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

    class Meta (object):
        abstract = True


class AttributeType   (EnumModel): pass
class DerangementType (EnumModel): pass
class FlawType        (EnumModel): pass
class MeritType       (EnumModel): pass
class SkillType       (EnumModel): pass
class Vice            (EnumModel): pass
class Virtue          (EnumModel): pass


class TraitTypeField (models.ForeignKey):
    def __init__ (self, related, **kwargs):
        return super(TraitTypeField, self).__init__(related, related_name = 'trait', **kwargs)


def _make_type_link (model_name):
    reverse_target = 'admin:traits_' + model_name + '_change'
    def type_link (self):
        return '<a href="{}">{}</a>'.format(
            reverse(reverse_target, args = (self.type.id,)),
            escape(self.type)
        )
    type_link.admin_order_field = 'type'
    type_link.allow_tags        = True
    type_link.short_description = 'Type'
    return type_link


class TraitModel (models.Model):
    enabled = models.BooleanField(default = True)
    name    = models.CharField(max_length = 255, unique = True)

    def __unicode__(self):
        return self.name

    class Meta (object):
        abstract = True


class Affiliation (TraitModel): pass


class Attribute (TraitModel):
    type = TraitTypeField(AttributeType)

    type_link = _make_type_link('attributetype')


class CharacterText (TraitModel):
    hide_from_player = models.BooleanField(default = False)


class CombatTrait (TraitModel): pass


class CreatureType (TraitModel):
    genealogy_name   = models.CharField(max_length = 255, null = True, blank = True)
    affiliation_name = models.CharField(max_length = 255, null = True, blank = True)
    subgroup_name    = models.CharField(max_length = 255, null = True, blank = True)
    power_name       = models.CharField(max_length = 255, null = True, blank = True)


class Derangement (TraitModel):
    type = TraitTypeField(DerangementType)
    requires_specification = models.BooleanField()

    type_link = _make_type_link('derangementtype')


class Flaw (TraitModel):
    type = TraitTypeField(FlawType)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()

    type_link = _make_type_link('flawtype')


class Genealogy (TraitModel): pass


class Merit (TraitModel):
    type = TraitTypeField(MeritType)
    allowed_ratings        = models.CommaSeparatedIntegerField(max_length = 255)
    requires_specification = models.BooleanField()
    requires_description   = models.BooleanField()

    type_link = _make_type_link('merittype')


class MiscTrait (TraitModel):
    requires_description = models.BooleanField()


class Power (TraitModel):
    rating = models.IntegerField(null = True, blank = True)
    group  = models.CharField(max_length = 255)


class Skill (TraitModel):
    type = TraitTypeField(SkillType)
    class Meta(object):
        ordering = ('name',)

class Subgroup (TraitModel): pass
