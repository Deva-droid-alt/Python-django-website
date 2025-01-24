# views.py
from django.shortcuts import render

def Firstpg(request):
    return render(request, 'home.html')

def trivandrum(request):
    return render(request, 'trivandrum.html')

def kollam(request):
    return render(request, 'kollam.html')

def kottayam(request):
    return render(request, 'kottayam.html')

def ekm(request):
    return render(request, 'ekm.html')

def thrissur(request):
    return render(request, 'thrissur.html')
