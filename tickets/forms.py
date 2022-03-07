from django import forms
from .models import Ticket, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ('This is where you can write your comment'),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'body', 'importance', 'attachment')
        labels = {
            'title': ('Title of your ticket'),
            'body': ('This is where you can write your comment'),
            'importance': ('How important is this for your work/order?'),
            'attachment': ('You can add you attchament here:')
        }