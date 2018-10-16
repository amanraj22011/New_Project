from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from.models import lenovothink
from .forms import lenovo_laptop
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def Home(request):
    all_laptops = lenovothink.objects.all()
    return render(request,'lenovo/home.html', {'all_laptops': all_laptops})

def detail(request, val):
    lenovo = lenovothink.objects.get(id = val)
    return render(request,'lenovo/detail.html',{'lenovo':lenovo})


def add_new(request):
    if request.method == 'POST':
        form = lenovo_laptop(request.POST)
        if form.is_valid():
            lenovo = form.save()
            lenovo.save()
            return redirect('/')
    else:
        form = lenovo_laptop()
        return render (request, "lenovo/edit_detail.html", {'form' : form})




def login_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, raw_password= raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'lenovo/login.html', {'form' : form})


def logout_form(request):
    logout(request)
    return redirect('/')
  