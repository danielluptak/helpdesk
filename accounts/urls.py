from django.urls import path
from .views import ITRegisterView, SignUpView

urlpatterns = [
    path('singup/', SignUpView.as_view(), name='signup'),
    path('register_it/', ITRegisterView.as_view(), name='register_it')
]
