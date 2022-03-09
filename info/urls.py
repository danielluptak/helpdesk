from django.urls import path
from .views import (
    InfoListView,
    InfoUpdateView,
    InfoDeleteView,
    InfoCreateView,
)
from . import views

urlpatterns = [
    path('info/<int:pk>/edit/',
        InfoUpdateView.as_view(), name='info_edit'),
    path('info/<int:pk>/delete/',
        InfoDeleteView.as_view(), name='info_delete'),
    path('info/new/', 
        InfoCreateView.as_view(), name='info_new'),

    path('', InfoListView.as_view(), name='info_list'),
    
    path('key', views.gen_secret_key)
]