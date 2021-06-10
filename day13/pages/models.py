from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.conf import settings

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    ip_addr = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pages")

    def __str__(self):
        return f'title: {self.title} / content: {self.content}'

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="comments") # models.SET_NULL
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    # related_name 지정 시 지정된 이름으로 page.comment를 역참조 할 수 있음
    # comment.page
    # page.comment_set
    # page.comments

    def __str__(self):
        return f'content: {self.content}'
