from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup_user,name='signup'),
    path('',views.home,name='homepage'),
    path('login/',views.login_user,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.userlogout,name='logout'),
    path('changepassword/',views.passchange,name='passchange1'),
    path('changepassword1/',views.passchangewithoutprev,name='passchange2')
]
