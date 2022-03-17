from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserITForm, EditProfileForm

from django.contrib.auth.mixins import LoginRequiredMixin 

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.instance.is_customer = True
        return super().form_valid(form)
    
class ITRegisterView(LoginRequiredMixin, CreateView):
    form_class = CustomUserITForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register_it.html'

    def form_valid(self, form):
        form.instance.is_it = True
        return super().form_valid(form)
    
class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user
    