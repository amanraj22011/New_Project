from django.shortcuts import render
from.models import lenovothink

def Home(request):
    all_laptops = lenovothink.objects.all()
    return render(request,'lenovo/home.html', {'all_laptops': all_laptops})

def detail(request, val):
    lenovo = lenovothink.objects.get(id = val)
    return render(request,'lenovo/detail.html',{'lenovo':lenovo})