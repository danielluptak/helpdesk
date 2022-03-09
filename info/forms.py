from socket import fromshare
from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('title','body',)
        labels = {
            'title': ('Title of your knowledge info'),
            'body': ('Body of information you are sharing')
        }