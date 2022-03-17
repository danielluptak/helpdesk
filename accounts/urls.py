from django.urls import path
from .views import ITRegisterView, SignUpView, UserEditView, ShowProfilePageView, ShowUsersProfilePageView

urlpatterns = [
    path('singup/', SignUpView.as_view(), name='signup'),
    path('register_it/', ITRegisterView.as_view(), name='register_it'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('profile/', ShowProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/profile/', ShowUsersProfilePageView.as_view(), name='someones_profile_page'),
]
