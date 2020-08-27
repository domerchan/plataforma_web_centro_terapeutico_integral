from django.shortcuts import render
from django.http import HttpResponse
from website.models import User
from website.models import Direction
from website.forms import UserForm
from django.shortcuts import redirect

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

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

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

def registrar(request):
    if request.method=="POST":
        nombres = request.POST["names"]
        apellidos = request.POST["lnames"]
        cedula = request.POST["id"]
        tel1 = request.POST["tel1"]
        tel2 = request.POST["tel2"]
        dir1 = request.POST["dir1"]
        dir2 = request.POST["dir2"]
        dir3 = request.POST["dir3"]
        dir4 = request.POST["dir4"]
        email = request.POST["email"]
        password = request.POST["password"]
        birth = request.POST["birth"]
        sex = request.POST["sex"]
        status = request.POST["status"]

        rol = request.POST["rol"]
        job = request.POST["job"]
        degree = request.POST["degree"]
        bio = request.POST["bio"]
        
        direccion=Direction(main_street=dir1, secondary_street=dir2, house_number=dir3, reference=dir4) 
        direccion.save()
        usuario=User(first_name=nombres, last_name=apellidos, identity_card=cedula, rol=rol, birth=birth, sex=sex, civil_status=status, phone_number_1=tel1, phone_number_2=tel2, email=email, direction=direccion, job_title=job, degree=degree, biography=bio)
        usuario.save()

        response = redirect('login')
        return response
    else:
        return render(request, "index.html")
