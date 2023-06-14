from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from django.utils.text import slugify

from ..account.models import CustomUserModel, CoursesModel
from .validators import validate_file_extension


class VideoModel(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', validators=[validate_file_extension], null=True)
    instructor = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='videos',
                                   limit_choices_to={"groups": 2})
    department = models.ForeignKey(CoursesModel, on_delete=models.CASCADE, related_name='videos', null=True)
    created_on = models.DateTimeField(editable=False)
    updated_on = models.DateTimeField(editable=False)

    class Meta:
        db_table = 'videos'
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        return slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        self.slug = self.get_slug()
        return super(VideoModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class VideoCommentModel(models.Model):
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='comments')
    video = models.ForeignKey(VideoModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_on = models.DateTimeField(editable=False)
    updated_on = models.DateTimeField(editable=False)

    class Meta:
        db_table = 'video_comments'
        verbose_name = 'Video Yorumu'
        verbose_name_plural = 'Video Yorumları'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()
        return super(VideoCommentModel, self).save(*args, **kwargs)

    def children(self):
        return VideoCommentModel.objects.filter(parent=self)

    @property
    def any_children(self):
        return VideoCommentModel.objects.filter(parent=self).exists()

    def __str__(self):
        return self.author.get_full_name()
