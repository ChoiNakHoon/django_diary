from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    descript = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.title}"{self.descript} - {self.cdate}'