from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.text import slugify
from ..courses.models import CoursesModel, CourseCategoriesModel, PeriodModel
from .abstracts import AbstractDatesModel
from .helpers import generate_student_number


class RolesModel(AbstractDatesModel):
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


class UserLinksModel(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    class Meta:
        db_table = 'users_links'
        verbose_name = 'Üye Profil Linki'
        verbose_name_plural = 'Üye Profil Linkleri'


class CustomUserModel(AbstractUser):
    username = models.CharField(max_length=120, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, verbose_name='Eposta Adresi')
    first_name = models.CharField(max_length=150, verbose_name='İsim')
    last_name = models.CharField(max_length=150, verbose_name='Soyisim')
    slug = AutoSlugField(populate_from='username', unique=True, editable=False)
    groups = models.ForeignKey(RolesModel, blank=True, on_delete=models.SET_NULL, null=True, default=1,
                               related_name='users',
                               verbose_name='Rol')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar',
                               default='default-avatar.jpg')
    social_links = models.ManyToManyField(UserLinksModel, blank=True, related_name='social_links')
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        verbose_name = 'Üye'
        verbose_name_plural = 'Üyeler'

    def __str__(self):
        return self.email

    def get_slug(self):
        slug = slugify(self.username.replace("ı", "i"))
        return slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        # Eposta adresinden otomatik username oluşturma
        if not self.username:
            self.username = slugify(self.email.split('@')[0])
        self.slug = self.get_slug()

        # Avatar atanmamışsa varsayılan avatarı atama
        if not self.avatar:
            self.avatar = 'default-avatar.jpg'
        super(CustomUserModel, self).save(*args, **kwargs)


class StudentModel(AbstractDatesModel):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='student_profile', verbose_name='Üye')
    student_no = models.CharField(max_length=11, verbose_name='Öğrenci Numarası', unique=True, blank=True)
    course = models.ForeignKey(CoursesModel, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='course_users', verbose_name='Kurs')
    period = models.ForeignKey(PeriodModel, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='period_users', verbose_name='Dönem')

    class Meta:
        db_table = 'students'
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'

    def save(self, *args, **kwargs):
        if not self.student_no:
            self.student_no = generate_student_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_full_name()


class InstructorModel(AbstractDatesModel):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='instructor_profile', verbose_name='Üye')
    courses = models.ManyToManyField(CoursesModel, blank=True, verbose_name='Bağlı Olduğu Kurslar')
    start_date = models.DateTimeField(null=True, verbose_name='Başlangıç Tarihi')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Ayrılış Tarihi')

    class Meta:
        db_table = 'instructors'
        verbose_name = 'Eğitmen'
        verbose_name_plural = 'Eğitmenler'

    def __str__(self):
        return self.user.get_full_name()
