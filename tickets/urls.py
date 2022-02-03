from django.urls import path
from .views import (
    TicketListView,
    TicketUpdateView,
    TicketDetailView,
    TicketDeleteView,
)


urlpatterns = [
    path('<int:pk>/edit/',
        TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/',
        TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/delete/',
        TicketDeleteView.as_view(), name='ticket_delete'),

    path('', TicketListView.as_view(), name='ticket_list'),
]