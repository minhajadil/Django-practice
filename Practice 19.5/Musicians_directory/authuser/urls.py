from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',views.UserLoginView.as_view(),name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout')
    path('logout/',views.userlogout,name='logout')
]
