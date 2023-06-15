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
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login',)}),
        ('Sosyal Bilgiler', {'fields': ('social_links', 'bio')}),

    )
    fieldsets += (
        (
            'Ek ayarlar',  # you can also use None
            {
                'fields': (
                    'avatar',
                ),
            },
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'groups'),
        }),
    )


class CustomGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


@admin.register(StudentModel)
class CustomStudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_no', 'course', 'period')


admin.site.register(InstructorModel)
admin.site.register(StaffModel)
admin.site.register(StaffDepartmentModel)
admin.site.register(UserLinksModel)

admin.site.unregister(Group)
admin.site.register(RolesModel, CustomGroupAdmin)
