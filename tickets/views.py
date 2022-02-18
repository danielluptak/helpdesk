from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.core.management.utils import get_random_secret_key
from django.http import HttpResponse 

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ('title',  'body', 'status', 'it_assigned')
    template_name = 'ticket_edit.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('ticket_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket_new.html'
    fields = ('title', 'body', 'importance', 'attachment')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def gen_secret_key(request):
    print(get_random_secret_key())
    return HttpResponse("Key generated")