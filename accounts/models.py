from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser (AbstractUser):
    is_customer = models.BooleanField('customer status', default=False)
    is_it = models.BooleanField('IT status', default=False)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")

    def __str__(self):
        return str(self.user)