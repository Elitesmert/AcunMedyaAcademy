from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.text import slugify


class PeriodModel(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'periods'
        verbose_name = 'Dönem'
        verbose_name_plural = 'Dönemler'


class RolesModel(models.Model):
    app_label = 'account'
    name = models.CharField(max_length=150, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Roles'
        verbose_name_plural = 'Roller'

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
        return super(RolesModel, self).save(*args, **kwargs)


class CoursesModel(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='lesson_images/', null=True)

    class Meta:
        db_table = 'courses'
        verbose_name = 'Sınıf'
        verbose_name_plural = 'Sınıflar'

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


class CustomUserModel(AbstractUser):
    email = models.EmailField(max_length=200, verbose_name='Eposta Adresi')
    first_name = models.CharField(max_length=150, verbose_name='İsim')
    last_name = models.CharField(max_length=150, verbose_name='Soyisim')
    slug = AutoSlugField(populate_from='username', unique=True, editable=False)
    groups = models.ForeignKey(RolesModel, blank=True, on_delete=models.SET_NULL, null=True, related_name='users',
                               verbose_name='Rol')
    courses = models.ManyToManyField(CoursesModel, related_name='users', verbose_name='Bölümü')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar',
                               default='default-avatar.jpg')
    birth_date = models.DateField(max_length=200, null=True, blank=True, verbose_name='Doğum Tarihi')
    github_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Github')
    linkedin_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='LinkedIn')
    instagram_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Instagram')

    class Meta:
        db_table = 'users'
        verbose_name = 'Üye'
        verbose_name_plural = 'Üyeler'

    def get_slug(self):
        slug = slugify(self.username.replace("ı", "i"))
        return slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        self.slug = self.get_slug()
        # Avatar atanmamışsa varsayılan avatarı atama
        if not self.avatar:
            self.avatar = 'default-avatar.jpg'
        super(CustomUserModel, self).save(*args, **kwargs)
