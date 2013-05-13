# DCMS auto-generated file
# 2013-05-13 11:58:31.554363

# # # # # # # # # # # # # # # # # # # # # # #
# DO NOT MODIFY THE CONTENTS OF THIS FILE!  #
# # # # # # # # # # # # # # # # # # # # # # #

# If you wish to alter it's contents modify either the source model, or the
# generating tool and then run `manage.py generate_classes` again.  (Don't
# forget to commit the newly generated files!)


from django.conf.urls import url

from character.views import CharacterDetail
from character.views import CharacterList

urls = [
  url(r'^Character/(?P<pk>[0-9]+)/$', CharacterDetail.as_view()),
  url(r'^Character/$',                CharacterList.as_view()),
]
