from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser (AbstractUser):
    is_customer = models.BooleanField('customer status', default=False)
    is_it = models.BooleanField('IT status', default=False)
    bio = models.CharField(max_length=1000, null=True, blank = True)
    position = models.TextField(max_length=50, null=True, blank = True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")

    # def __str__(self):
    #         return str(self.user)