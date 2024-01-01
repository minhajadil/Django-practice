from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import MusicianDB

# Create your views here.

def delete_musician(request,id):
    musician= MusicianDB.objects.get(pk=id)
    musician.delete()

    
    return redirect('homepage')



def edit_musician(request,id):

    musician = MusicianDB.objects.get(pk=id)
    form = MusicianForm(instance=musician)



    if request.method=='POST':
        form = MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request,'musician.html',{'form':form})

def add_musician(request):
    if request.method=='POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else :
        form = MusicianForm()
    return render(request,'musician.html',{'form':form})

