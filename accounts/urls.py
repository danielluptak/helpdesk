from django.urls import path
from .views import ITRegisterView, SignUpView, UserEditView

urlpatterns = [
    path('singup/', SignUpView.as_view(), name='signup'),
    path('register_it/', ITRegisterView.as_view(), name='register_it'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
