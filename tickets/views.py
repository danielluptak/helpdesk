from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Ticket

class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list.html'

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'

class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ('title',  'body', 'status', 'it_assigned')
    template_name = 'ticket_edit.html'

class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('ticket_list')

class TicketCreateView(CreateView):
    model = Ticket
    template_name = 'ticket_new.html'
    fields = ('title', 'body', 'author', 'importance',)