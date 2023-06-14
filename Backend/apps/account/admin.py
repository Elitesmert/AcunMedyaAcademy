from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    list_filter = ('username', 'email')
    filter_horizontal = []

    fieldsets = UserAdmin.fieldsets + (
        (
            'Ek ayarlar',  # you can also use None
            {
                'fields': (
                    'department',
                    'avatar',
                    'period'
                ),
            },
        ),
        (
            'Sosyal Medya Hesapları',  # you can also use None
            {
                'fields': (
                    'github_link',
                    'linkedin_link',
                    'instagram_link'
                ),
            },
        ),
    )


class CustomGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


admin.site.unregister(Group)
admin.site.register(RolesModel, CustomGroupAdmin)
