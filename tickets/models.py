from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to="images", null=True, blank=True)
    status = models.CharField(max_length=30)
    importance = models.CharField(max_length=50)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    it_assigned = models.ForeignKey(
        'accounts.CustomUser',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name= 'it_for_ticket'
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ticket_detail", args=[str(self.id)])
    