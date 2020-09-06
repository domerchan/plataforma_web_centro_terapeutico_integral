from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin
from website.models import User
from website.models import Direction
from website.forms import UserForm

from django.db.models import Count

from website.models import Therapeutic_center
from website.models import Forum_entry
from website.models import Forum_response
from website.forms import UserForm


# Create your views here.
center_data = Therapeutic_center.objects.first()

def about(request):
    return render(request, 'about.html', {'center_data':center_data})

def blog(request):
    entries = Forum_entry.objects.all().annotate(responses=Count('forum_response'))
    return render(request, 'blog.html', {'center_data':center_data, 'entries':entries})

def blogsingle(request):
    return render(request, 'blog-single.html', {'center_data':center_data})

def contact(request):
    return render(request, 'contact.html', {'center_data':center_data})

def directory(request):
    return render(request, 'directory.html', {'center_data':center_data})

def donations(request):
    return render(request, 'donations.html', {'center_data':center_data})

def index(request):
    return render(request, 'index.html', {'center_data':center_data})

def information(request):
    return render(request, 'information.html', {'center_data':center_data})

def login(request):
    return render(request, 'login.html', {'center_data':center_data})

def registro(request):
    return render(request, 'registro.html', {'center_data':center_data})

def report(request):
    return render(request, 'report.html', {'center_data':center_data})

def therapies(request):
    return render(request, 'therapies.html', {'center_data':center_data})

def tips(request):
    return render(request, 'tips.html', {'center_data':center_data})

def training(request):
    return render(request, 'training.html', {'center_data':center_data})

def tutorial(request):
    return render(request, 'tutorial.html', {'center_data':center_data})

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
        password2 = request.POST["password2"]
        birth = request.POST["birth"]
        sex = request.POST["sex"]
        status = request.POST["status"]

        rol = request.POST["rol"]
        job = request.POST["job"]
        degree = request.POST["degree"]
        bio = request.POST["bio"]
        
        try:
            user = User.objects.get(email=email)
            messages.success(request, 'Usuario previamente registrado')
            response = redirect('registro')
            return response
        except:
            if(password == password2):
                direccion=Direction(main_street=dir1, secondary_street=dir2, house_number=dir3, reference=dir4) 
                direccion.save()
                usuario=User(first_name=nombres, last_name=apellidos, identity_card=cedula, rol=rol, birth=birth, sex=sex, civil_status=status, phone_number_1=tel1, phone_number_2=tel2, email=email, password=password, direction=direccion, job_title=job, degree=degree, biography=bio)
                usuario.save()
                request.session['user_email'] = usuario.email
                request.session['user_rol'] = usuario.rol
                response = redirect('index')
                return response
            else:
                messages.success(request, 'La contraseña no es igual')
                response = redirect('registro')
                return response
    else:
        return render(request, "index.html")

def iniciarSesion(request):
    if request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
        except:
            messages.success(request, 'Usuario o Contraseña Incorrecto')
            response = redirect('login')
            return response
        
        if user.password != password:
            messages.success(request, 'Usuario o Contraseña Incorrecto')        
            response = redirect('login')
            return response
        else: 
            user = User.objects.get(email=email)
            request.session['user_email'] = user.email
            request.session['user_rol'] = user.rol
            usuario = request.session['user_email']
            if 'user_email' in request.session:
                #return HttpResponse(usuario)
                usuarioGlob = User.objects.get(email=request.session['user_email'])
                return redirect('index')
                #return render(request, 'index.html', context) 
            else:
                response = redirect('index')
                return HttpResponse("Incorrecto")
                #return response
            

def logout(request):
    if 'user_email' in request.session:
        del request.session['user_email']
        response = redirect('login')
        return response
    else:
        response = redirect('index')
        return response

    
def enviarCorreo(request):
    if request.method=="POST":
        if 'user_email' in request.session:
            subject=request.POST["asunto"]
            message=request.POST["mensaje"] + " " + request.session["user_email"]
            email_from=settings.EMAIL_HOST_USER
            recipient_list=['alejo.sebas99@outlook.com']

            send_mail(subject, message, email_from, recipient_list)
            return HttpResponse("Correcto")
    
    return HttpResponse("Incorrecto")

def comment(request, email, entry):
    en = Forum_entry.objects.filter(id=entry).first()
    user = User.objects.filter(email=email).first()
    if request.method=="POST":
        rp = request.POST["response"]
        
        res = Forum_response(entry=en, user=user, response=rp)
        res.save()

        return redirect('/blog-single.html/'+str(entry))
    else:
        return render(request, "index.html")

def showForum(request, id):
    forum_responses = Forum_response.objects.filter(entry=id)
    entry = Forum_entry.objects.filter(id=id).first()
    entries = Forum_entry.objects.reverse()[:5].annotate(responses=Count('forum_response'))
    count_responses = Forum_response.objects.filter(entry=id).count()
    return render(request, 'blog-single.html', {'center_data':center_data, 'entry':entry, 'responses':forum_responses, 'entries':entries, 'count_responses':count_responses})
