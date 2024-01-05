from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import MusicianDB
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required(login_url='login'),name='dispatch')
class delete_musician(DeleteView):
    model = MusicianDB
    template_name= 'delete.html'
    success_url= reverse_lazy('homepage')
    pk_url_kwarg=id


@method_decorator(login_required(login_url='login'),name='dispatch')
class edit_musician(UpdateView):
    model = MusicianDB
    form_class = MusicianForm
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

@method_decorator(login_required(login_url='login'),name='dispatch')
class add_musician(CreateView):
    model = MusicianDB
    template_name = 'musician.html'
    form_class= MusicianForm
    success_url= reverse_lazy('homepage')