from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')

def pricing(request):
    return render(request, 'pricing.html')

def teacher(request):
    return render(request, 'teacher.html')