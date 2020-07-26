from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html')

def directory(request):
    return render(request, 'directory.html')

def donations(request):
    return render(request, 'donations.html')

def index(request):
    return render(request, 'index.html')

def information(request):
    return render(request, 'information.html')

def report(request):
    return render(request, 'report.html')

def therapies(request):
    return render(request, 'therapies.html')

def tips(request):
    return render(request, 'tips.html')

def training(request):
    return render(request, 'training.html')

def tutorial(request):
    return render(request, 'tutorial.html')