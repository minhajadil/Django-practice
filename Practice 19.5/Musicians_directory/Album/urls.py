from django.urls import path
from .import views
urlpatterns = [
    path('edit/<int:id>', views.edit_album.as_view(),name='edit_album'),
    path('add/', views.add_album.as_view(),name='add_album'),
    path('delete/<int:id>', views.delete_album.as_view(),name='delete_album')
]
