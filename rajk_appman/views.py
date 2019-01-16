from django.shortcuts import render
from .models import App

def home(request):
    return render(request, 'rajk-appman/home.html',
                   {'applist': App.objects.all()})