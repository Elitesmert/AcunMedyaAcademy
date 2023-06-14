from django.contrib import admin
from .models import CoursesModel, CourseCategoriesModel, PeriodModel

@admin.register(PeriodModel)
class CustomPeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')


@admin.register(CoursesModel)
class CustomCoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(CourseCategoriesModel)
class CustomCourseCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')