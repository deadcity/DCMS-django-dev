from django.shortcuts import render

from rest_framework.renderers import JSONRenderer

from character.models import Character
from traits.models import Affiliation, CreatureType, Genealogy, Subgroup, Vice, Virtue
import traits.serializers


def character_list (request):
    return render(request, 'character/character_list.html', {
        'character_list' : [{
            'json'        : JSONRenderer().render(Character.Serializer(character).data),
            'can_submit'  : True,
            'can_edit'    : True,
            'can_disable' : True,
        } for character in Character.objects.all()],
        'Affiliation'  : { 'objects': Affiliation  .objects.all(), 'Serializer': Affiliation  .Serializer },
        'CreatureType' : { 'objects': CreatureType .objects.all(), 'Serializer': CreatureType .Serializer },
        'Genealogy'    : { 'objects': Genealogy    .objects.all(), 'Serializer': Genealogy    .Serializer },
        'Subgroup'     : { 'objects': Subgroup     .objects.all(), 'Serializer': Subgroup     .Serializer },
        'Vice'         : { 'objects': Vice         .objects.all(), 'Serializer': Vice         .Serializer },
        'Virtue'       : { 'objects': Virtue       .objects.all(), 'Serializer': Virtue       .Serializer },
    })
