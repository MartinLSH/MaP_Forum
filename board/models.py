from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_comment = models.BooleanField(default=True)  # 답변가능 여부

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('board:index', args=[self.name])
    
def user_directory_path(instance, filename):
    return f'images/{instance.category.__str__()}/{instance.id}/{filename}'

class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = RichTextUploadingField(null=True)
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, blank=True, related_name='voter')
    notice = models.BooleanField(default=False)
    view_cnt = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_post')
    
    def filename(self):
        return os.path.basename(self.file.name)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
