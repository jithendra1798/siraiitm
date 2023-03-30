from django.contrib import admin
from siraconfig.models import Defaults
from django.contrib.admin import ModelAdmin

# Register your models here.

class DefaultsAdmin(ModelAdmin):
    list_display = (
        'default_site_name', 'support_mobile',
        'support_email'
        )
    readonly_fields = ('default_user_photo_image_tag', 'default_site_logo_image_tag',
                       'default_site_favicon_image_tag',)

    fieldsets = (
        (None, {
            'fields': ( 'default_site_name', 'support_mobile',
                       'support_email', 'default_portal_name',
                       'default_portal_shortform')
        }),
        ('Site Images', {
            'fields': ('default_user_photo', 'default_site_logo',
                       'default_site_favicon',
                       'default_user_photo_image_tag', 'default_site_logo_image_tag',
                       'default_site_favicon_image_tag',)
        }),
        # ('Additional Info', {
        #     # 'classes': ('collapse',),
        #     'fields': ('id', )
        # })
    )
admin.site.register(Defaults, DefaultsAdmin)
