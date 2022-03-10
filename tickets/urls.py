from django.urls import path
from .views import (
    TicketListView,
    TicketUpdateView,
    TicketDetailView,
    TicketDeleteView,
    TicketCreateView,
    TicketCommentView,
    OpenTicketListView,
)
from . import views 


urlpatterns = [
    path('ticket/<int:pk>/edit/',
        TicketUpdateView.as_view(), name='ticket_edit'),
    path('ticket/<int:pk>/',
        TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/delete/',
        TicketDeleteView.as_view(), name='ticket_delete'),
    path('ticket/new/', 
        TicketCreateView.as_view(), name='ticket_new'),
    path('ticket/<int:pk>/comment/', 
        TicketCommentView.as_view(), name='add_comment'),
    path('ticket/open/', 
        OpenTicketListView.as_view(), name='ticket_open'),

    path('', TicketListView.as_view(), name='ticket_list'),
    
    path('key', views.gen_secret_key)
]