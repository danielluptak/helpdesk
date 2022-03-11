from django.urls import path
from .views import (
    TicketListView,
    TicketUpdateView,
    TicketDetailView,
    TicketDeleteView,
    TicketCreateView,
    TicketCommentView,
    TicketCommentDeleteView,
    OpenTicketListView,
    InProgressTicketListView,
    ClosedTicketListView,
)
from . import views 


urlpatterns = [
    # tickets core urls
    path('ticket/<int:pk>/edit/',
        TicketUpdateView.as_view(), name='ticket_edit'),
    path('ticket/<int:pk>/',
        TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/delete/',
        TicketDeleteView.as_view(), name='ticket_delete'),
    path('ticket/new/', 
        TicketCreateView.as_view(), name='ticket_new'),
    
    # comments urls
    path('ticket/<int:pk>/comment/', 
        TicketCommentView.as_view(), name='add_comment'),
    path('<slug>/<int:pk>/delete/',
        TicketCommentDeleteView.as_view(), name='delete_comment'),
    
    # ticket lists urls
    path('ticket/open/',
        OpenTicketListView.as_view(), name='ticket_open'),
    path('ticket/progress/', 
        InProgressTicketListView.as_view(), name='ticket_progress'),
    path('ticket/closed/', 
        ClosedTicketListView.as_view(), name='ticket_closed'),

    path('', TicketListView.as_view(), name='ticket_list'),
    
    path('key', views.gen_secret_key)
]