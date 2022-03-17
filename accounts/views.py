from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserITForm, EditProfileForm

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.shortcuts import get_object_or_404

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
    
class ShowProfilePageView(DetailView):
    model = CustomUser
    template_name = 'registration/user_profile.html'
    
    def get_object(self):
        return self.request.user

class ShowUsersProfilePageView(DetailView):
    model = CustomUser
    template_name = 'registration/different_user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        # users = CustomUser.objects.all()
        context = super(ShowUsersProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])

        context["page_user"] = page_user
        
        return context
    
    
    
    
    
    # def profile(request, pk):
    #     request.instance.ticket_id = kwargs['pk']
    #     form.instance.author_id = self.request.user.pk
    #     return super().form_valid(request)
    
    # def profile(request):
    #     return render(request)
    
    # def get_user_profile(request, username):
    #     user = CustomUser.objects.get(username=username)
    #     return render(request, '<int:pk>/different_user_profile.html', {"user":user})
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ShowUsersProfilePageView, self).get_context_data(*args, **kwargs)
    #     get_object_or_404(CustomUser, id=self.kwargs['pk'])