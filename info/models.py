from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse


class Info(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.title
    
    