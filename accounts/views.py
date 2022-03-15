from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
# from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from django.shortcuts import get_object_or_404

from .forms import CustomUserCreationForm, CustomUserITForm, EditProfileForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
 
    def form_valid(self, form):
        form.instance.is_customer = True
        return super().form_valid(form)
    
class UserEditView(UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user

class ITRegisterView(CreateView):
    form_class = CustomUserITForm
    success_url = reverse_lazy('home')
    template_name = 'registration/register_it.html'

    def form_valid(self, form):
        form.instance.is_it = True
        return super().form_valid(form)

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
    