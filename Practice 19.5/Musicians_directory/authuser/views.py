from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout




# Create your views here.

class UserLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)



def userlogout(request):
    logout(request)
    return redirect('homepage')

