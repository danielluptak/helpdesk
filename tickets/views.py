from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Ticket, Comment
from .forms import CommentForm, TicketForm, TicketEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.core.management.utils import get_random_secret_key
from django.http import HttpResponse 

from django.db.models.signals import post_delete
from django.dispatch import receiver

# all tickets
class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    ordering = ['-id']
    
# open tickets
class OpenTicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    ordering = ['-id']
 
    def get_queryset(self):
        return Ticket.objects.filter(status='new')
    
# in progress tickets
class InProgressTicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    ordering = ['-id']

    def get_queryset(self):
        return Ticket.objects.filter(status='progress')

# closed  tickets

class ClosedTicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    ordering = ['-id']

    def get_queryset(self):
        return Ticket.objects.filter(status='closed')


# ticket detail
class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

# ticket edit
class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    # fields = ('title',  'body', 'status', 'it_assigned')
    form_class = TicketEditForm
    template_name = 'tickets/ticket_edit.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# ticket delete
class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    fields = '__all__'
    template_name = 'tickets/ticket_delete.html'
    success_url = reverse_lazy('ticket_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# new ticket creation
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_new.html'
    # fields = ('title', 'body', 'importance', 'attachment')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return reverse_lazy('ticket_detail', kwargs={'pk':self.kwargs['pk']})

# ticket comment
class TicketCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'tickets/add_comment.html'
    #fields = ('body',)
    # success_url = reverse_lazy('ticket_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.ticket_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'pk':self.kwargs['pk']})


class TicketCommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    fields = '__all__'
    template_name = 'tickets/delete_comment.html'
    # success_url = reverse_lazy('ticket_list')
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'pk':self.object.ticket_id})


def gen_secret_key(request):
    print(get_random_secret_key())
    return HttpResponse("Key generated")