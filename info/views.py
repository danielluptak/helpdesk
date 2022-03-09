from http.client import HTTPResponse
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Info
from .forms import InfoForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.core.management.utils import get_random_secret_key
from django.http import HttpResponse 

class InfoCreateView(LoginRequiredMixin, CreateView):
    model = Info
    form_class = InfoForm
    template_name = 'info/info_new.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class InfoListView(LoginRequiredMixin, ListView):
    model = Info
    template_name = 'info/info_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    ordering = ['-id']
    
class InfoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Info
    fields = ('title', 'body',)
    template_name = 'info/info_edit.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user    

class InfoDeleteView(LoginRequiredMixin, DeleteView):
    model = Info
    fields = '__all__'
    template_name = 'info/info_delete.html'
    success_url = reverse_lazy('info_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

def gen_secret_key(request):
    print(get_random_secret_key())
    return HttpResponse("Key generated")