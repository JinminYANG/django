from django.db import models
import json

# Create your models here.
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
    team_color = models.CharField(verbose_name='COLOR', max_length=25, default='rgba(240, 116, 137, 1)', null=True)

