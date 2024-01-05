from django.shortcuts import render
from Album.models import AlbumDB


def home(request):
    db = AlbumDB.objects.all()
    return render(request,'home.html',{'db':db})