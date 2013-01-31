from django.contrib import admin
from traits.models import AttributeType, Attribute


class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'type')
    list_filter = ('enabled', 'type',)


admin.site.register(AttributeType, AttributeTypeAdmin)
admin.site.register(Attribute,     AttributeAdmin)
