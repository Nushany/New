from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import SignUpForm

def index(request):
    return render(request, 'shopapp/index.html')

def biology(request):
    return render(request, 'shopapp/biology.html')

def chemistry(request):
    return render(request, 'shopapp/chemistry.html')

def list(request):
    return render(request, 'shopapp/list.html')

def profile(request):
    return render(request, 'shopapp/profile.html')

def info(request):
    return render(request, 'shopapp/info.html')


def signup(request):
    return render(request, 'shopapp/signup.html')