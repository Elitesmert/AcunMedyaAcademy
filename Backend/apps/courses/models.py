from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class PeriodModel(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'courses_periods'
        verbose_name = 'Dönem'
        verbose_name_plural = 'Dönemler'


class CourseCategoriesModel(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='course_categories_images/', null=True, blank=True)

    class Meta:
        db_table = 'course_categories'
        verbose_name = 'Kurs Kategorisi'
        verbose_name_plural = 'Kurs Kategorileri'

    def get_slug(self):
        slug = slugify(self.name.replace("ı", "i"))
        return slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        self.slug = self.get_slug()
        super(CourseCategoriesModel, self).save(*args, **kwargs)


class CoursesModel(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='lesson_images/', null=True, blank=True)
    category = models.ForeignKey(CourseCategoriesModel, on_delete=models.CASCADE, related_name='courses', null=True)

    class Meta:
        db_table = 'courses'
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'

    def __str__(self):
        return self.name

    def get_slug(self):
        slug = slugify(self.name.replace("ı", "i"))
        return slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        self.slug = self.get_slug()
        return super(CoursesModel, self).save(*args, **kwargs)
