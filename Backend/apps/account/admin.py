from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'slug')
    search_fields = ('username', 'email', 'slug')
    ordering = ['email']
    list_filter = ('email', 'date_joined')
    filter_horizontal = []
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Grup Ayarları', {'fields': ('groups',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    fieldsets += (
        (
            'Ek ayarlar',  # you can also use None
            {
                'fields': (
                    'courses',
                    'avatar',
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

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


class CustomGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


admin.site.unregister(Group)
admin.site.register(RolesModel, CustomGroupAdmin)
