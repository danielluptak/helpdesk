from django import forms
from .models import Ticket, Comment
from accounts.models import CustomUser

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
            'body': ('This is where you can write your body of text'),
            'importance': ('How important is this for your work/order?'),
            'attachment': ('You can add you attchament here:')
        }

class TicketEditForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title',  'body', 'status', 'it_assigned')
