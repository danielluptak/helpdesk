from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser (AbstractUser):
    is_customer = models.BooleanField('customer status', default=False)
    is_it = models.BooleanField('IT status', default=False)
