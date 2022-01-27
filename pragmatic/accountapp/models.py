from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django import forms
import json

# Create your models here.
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
    team_color = models.CharField(verbose_name='COLOR', max_length=25, default='rgba(240, 116, 137, 1)', null=True)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # redirect시 활용
        return reverse('account:post_detail', args=[self.id])


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')
