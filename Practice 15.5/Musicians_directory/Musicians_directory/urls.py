from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homepage'),
    path('album/',include('Album.urls')),
    path('musician/',include('Musician.urls')),
]
