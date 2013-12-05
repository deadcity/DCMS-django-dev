from django.core.urlresolvers import reverse
from django.template.defaultfilters import escape


def make_admin_link (Model, field_name):
    reverse_target = 'admin:{}_{}_change'.format(
        Model._meta.app_label,
        Model._meta.model_name
    )
    def admin_link (self, obj):
        return '<a href="{}">{}</a>'.format(
            reverse(reverse_target, args = (getattr(obj, field_name).id,)),
            escape(getattr(obj, field_name))
        )
    admin_link.admin_order_field = field_name
    admin_link.allow_tags        = True
    admin_link.short_description = Model._meta.verbose_name
    return admin_link
