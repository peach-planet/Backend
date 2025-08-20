from django.db import models
from django.conf import settings  

# Create your models here.


class Blog(models.Model):
    image=models.ImageField(verbose_name='이미지', null=True, blank=True)
    content=models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count=models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='작성자', null=True, blank=True)

# 댓글 기능 있으면 추가함
# class Comment(models.Model):
