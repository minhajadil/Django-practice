from django.shortcuts import render,redirect
from .forms import UserForm,datachange
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup_user(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
           
            form.save()
            return redirect('login')
    else :
        form =UserForm()
    return render(request,'signup.html',{'form':form})


def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = name , password=user_password)
            if user is not None:
                login(request,user)
                messages.success(request, "Logged in Successfully")
                return redirect('profile')
            else :
                return redirect('login')
    else :
        form = AuthenticationForm()
    
    return render (request,'login.html',{'form':form})

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')
   
@login_required(login_url='login')
def userlogout(request):
    logout(request)
    messages.warning(request,'Logged out Successfully')
    return redirect('homepage')

@login_required(login_url='login')
def passchange(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else :
        form = PasswordChangeForm(user=request.user)
    return render(request,'changepassword.html',{'form':form})

@login_required(login_url='login')
def passchangewithoutprev(request):
    if request.method=='POST':
        form =SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else :
        form = SetPasswordForm(user=request.user)
    return render(request,'changepassword.html',{'form':form})
    

def home(request):
    return render(request,'home.html')