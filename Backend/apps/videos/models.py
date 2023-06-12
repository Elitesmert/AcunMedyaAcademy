from django.db import models
from autoslug import AutoSlugField
from ..account.models import CustomUserModel, DepartmentModel


class VideoModel(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    instructor = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='videos',
                                   limit_choices_to={"groups": 2})
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, related_name='videos', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'videos'
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'

    def __str__(self):
        return self.title


class VideoCommentModel(models.Model):
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='comments')
    video = models.ForeignKey(VideoModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'video_comments'
        verbose_name = 'Video Yorumu'
        verbose_name_plural = 'Video Yorumları'

    def __str__(self):
        return self.author.get_full_name()
