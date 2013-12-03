from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from character import models


def is_storyteller (user):
    if user.groups.filter(id = 1).exists():
        return True
    return False


class CharacterPermission (BasePermission):
    def has_object_permission (self, request, view, obj):
        # Storytellers always have all permissions with their characters.
        if is_storyteller(request.user):
            return True

        # Only the character owner may access this character (except for STs).
        if request.user != obj.user:
            return False

        # Owner has universal read access.
        if request.method in SAFE_METHODS:
            return True

        # Owner can only edit when CharacterStatus.EDITING.
        return obj.status == models.CharacterStatus.EDITING


class CharacterTraitPermission (BasePermission):
    def has_object_permission (self, request, view, obj):
        # Storytellers always have all permissions with their characters.
        if is_storyteller(request.user):
            return True

        # Only the character owner may access this character (except for STs).
        if request.user != obj.character.user:
            return False

        # Owner has universal read access.
        if request.method in SAFE_METHODS:
            return True

        # Owner can only edit when CharacterStatus.EDITING.
        return obj.character.status == models.CharacterStatus.EDITING


character_permissions       = (IsAuthenticated, CharacterPermission)
character_trait_permissions = (IsAuthenticated, CharacterTraitPermission)
