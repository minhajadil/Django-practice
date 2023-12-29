from django.shortcuts import render
from .forms import PracticeForm

# Create your views here.


def home(request):
    form = PracticeForm

    return render(request,'first_app/home.html',{'forms' : form})