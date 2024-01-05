from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumDB

from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@method_decorator(login_required(login_url='login'),name='dispatch')
class add_album(CreateView):
    model = AlbumDB
    template_name = 'album.html'
    form_class= AlbumForm
    success_url= reverse_lazy('homepage')




@method_decorator(login_required(login_url='login'),name='dispatch')
class edit_album(UpdateView):
    model = AlbumDB
    form_class = AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    

@method_decorator(login_required(login_url='login'),name='dispatch')
class delete_album(DeleteView):
    model = AlbumDB
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'