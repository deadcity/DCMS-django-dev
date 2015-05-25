## @module characters.views
#  Provides view functions and classes related to character management.


from datetime import datetime
from itertools import chain

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from characters.models import Character
from dsqla.models import ModelEncoder
from dsqla.session import session


class HttpResponseUnauthorized (HttpResponse):
    status_code = 401


@login_required
def character_list (self, request):
    characters = session.query(Character)

    return render(request, 'characters/character_list.html', {
        'characters': characters,
        'records': chain(
            set(character.creature_type for character in characters),
            set(character.genealogy     for character in characters),
            set(character.affiliation   for character in characters),
            set(character.subgroup      for character in characters),
            set(character.virtue        for character in characters),
            set(character.vice          for character in characters),
        ),
    })


@login_required
@require_http_methods(['PUT'])
def submit_character (self, request, id):
    character = session.query(Character).get(int(id))
    if character.user_id != request.user.id:
        return HttpResponseUnauthorized(
            "Must be the character's owner to submit.",
            content_type = 'application/json'
        )

    if character.status != Character.Status.EDITING:
        return HttpResponseForbidden(
            "Character must have a status of 'EDITING' to submit.",
            content_type = 'application/json'
        )

    character.status = Character.Status.SUBMITTED
    character.date_submitted = datetime.now()

    return JsonResponse(
        character.to_dict(),
        safe = False,
        encoder = ModelEncoder
    )


def storyteller_or_editing_owner (request, character, action):
    # TODO(emery): check if user has storyteller permissions on this character

    if character.user_id != request.user.id:
        return HttpResponseUnauthorized(
            "Must be the character's owner to {}.".format(action),
            content_type = 'application/json'
        )

    if character.status != Character.Status.EDITING:
        return HttpResponseForbidden(
            "Character must have a status of 'EDITING' to {}.".format(action),
            content_type = 'application/json'
        )

    return None


@login_required
@require_http_methods(['PUT'])
def disable_character (self, request, id):
    character = session.query(Character).get(int(id))

    if character.enabled is False:
        return HttpResponseForbidden(
            'Character already disabled.',
            content_type = 'application/json'
        )

    response = storyteller_or_editing_owner(request, character, 'disable')
    if response:
        return response

    character.enabled = False

    return JsonResponse(
        character.to_dict(),
        safe = False,
        encoder = ModelEncoder
    )


@login_required
@require_http_methods(['PUT'])
def enable_character (self, request, id):
    character = session.query(Character).get(int(id))

    if character.enabled is False:
        return HttpResponseForbidden(
            'Character already enabled.',
            content_type = 'application/json'
        )

    response = storyteller_or_editing_owner(request, character, 'enable')
    if response:
        return response

    character.enabled = True

    return JsonResponse(
        character.to_dict(),
        safe = False,
        encoder = ModelEncoder
    )
