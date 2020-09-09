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
from PIL import Image
from website.models import Directory

from website.forms import UserForm

from django.db.models import Count

from website.models import User
from website.models import Direction
from website.models import Patient
from website.models import Post
from website.models import Relationship
from website.models import Therapy_local
from website.models import Therapy_live
from website.models import Therapeutic_center
from website.models import Disability_card
from website.models import Forum_entry
from website.models import Forum_response
from website.forms import UserForm


# Create your views here.
center_data = Therapeutic_center.objects.first()

def about(request):
    return render(request, 'about.html', {'center_data':center_data})

def forum(request):
    entries = Forum_entry.objects.all().annotate(responses=Count('forum_response'))
    return render(request, 'forum.html', {'center_data':center_data, 'entries':entries})

def forumEntry(request):
    return render(request, 'forum-entry.html', {'center_data':center_data})

def contact(request):
    return render(request, 'contact.html', {'center_data':center_data})

def directory(request):
    lugar = Directory.objects.all()
    return render(request, 'directory.html', {'center_data':center_data, 'directorios': lugar})

def donations(request):
    return render(request, 'donations.html', {'center_data':center_data})

def index(request):
    terapias = [] 
    #Therapy_live.objects.all()
    try:
        usuario = User.objects.get(email=request.session['user_email'])
        terapiasGrupales = Therapy_live.objects.all()
        if usuario.rol == "RP":
            terapias = Therapy_live.objects.all()
        else:
            for terapia in terapiasGrupales:
                if usuario == terapia.therapist:
                    terapias.append(terapia)
                    
    except:
        terapias = Therapy_live.objects.all()

    return render(request, 'index.html', {'center_data':center_data, 'terapias':terapias})

def information(request):
    return render(request, 'information.html', {'center_data':center_data})

def login(request):
    return render(request, 'login.html', {'center_data':center_data})

def pacientes(request):
    pacientes = []
    aprobados = []
    pacientesTerapeuta = []
    relaciones = Relationship.objects.all()
    terapias = Therapy_local.objects.all()

    for rel in relaciones:
        try:
            if rel.representative == User.objects.get(email=request.session['user_email']):
                pacientes.append(rel.patient)
    
        except:
            response = redirect('login')
            return response

    for ter in terapias:
        try:
            if ter.patient in pacientes:
                aprobados.append(ter.patient)
                pacientes.remove(ter.patient)
            if ter.therapist == User.objects.get(email=request.session['user_email']):
                pacientesTerapeuta.append(ter.patient)
        except:
            response = redirect('login')
            return response

    return render(request, 'pacientes.html', {'center_data':center_data, 'pacientes':pacientes, 'aprobados':aprobados, 'terapias':terapias, 'pacientesTerapeuta':pacientesTerapeuta})

def perfil(request):
    try:
        usuario = User.objects.get(email=request.session['user_email'])
    except:
        response = redirect('login')
        return response
    return render(request, 'perfil.html', {'center_data':center_data, 'usuario':usuario})

def perfilPaciente(request, id):
    try:
        paciente = Patient.objects.get(id=id)
        discapacidad = Disability_card.objects.get(patient=paciente)

        if discapacidad.disability_type == "HE":
            discapacidad.disability_type = "Discapacidad Auditiva"
        if discapacidad.disability_type == "PH":
            discapacidad.disability_type = "Discapacidad Física"
        if discapacidad.disability_type == "IN":
            discapacidad.disability_type = "Discapacidad Intelectual"
        if discapacidad.disability_type == "LA":
            discapacidad.disability_type = "Discapacidad del Lenguaje"
        if discapacidad.disability_type == "PS":
            discapacidad.disability_type = "Discapacidad Psicosocial"
        if discapacidad.disability_type == "VI":
            discapacidad.disability_type = "Discapacidad Visual"
        
        if paciente.parish_type == "UB":
            paciente.parish_type = "Urbana"
        if paciente.parish_type == "RU":
            paciente.parish_type = "Rural"

        if paciente.educational_institution_type == "IN":
            paciente.educational_institution_type = "Inclusiva"
        if paciente.educational_institution_type == "SP":
            paciente.educational_institution_type = "Especializada"
        if paciente.educational_institution_type == "RE":
            paciente.educational_institution_type = "Regular"

    except:
        response = redirect('pacientes')
        return response
    return render(request, 'perfil-paciente.html', {'center_data':center_data, 'paciente':paciente, 'discapacidad': discapacidad})

def registro(request):
    return render(request, 'registro.html', {'center_data':center_data})

def registroPaciente(request):
    return render(request, 'registro-paciente.html', {'center_data':center_data})

def report(request):
    return render(request, 'report.html', {'center_data':center_data})

def therapies(request):
    terapias = [] 
    #Therapy_live.objects.all()
    try:
        usuario = User.objects.get(email=request.session['user_email'])
        terapiasGrupales = Therapy_live.objects.all()
        if usuario.rol == "RP":
            terapias = Therapy_live.objects.all()
        else:
            for terapia in terapiasGrupales:
                if usuario == terapia.therapist:
                    terapias.append(terapia)

    except:
        response = redirect('login')
        return response

    return render(request, 'therapies.html', {'center_data':center_data, 'terapias':terapias})

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'center_data':center_data, 'posts':posts})

def training(request):
    return render(request, 'training.html', {'center_data':center_data})

def tutorial(request):
    return render(request, 'tutorial.html', {'center_data':center_data})

def disabilities(request):
    return render(request, 'disabilities.html', {'center_data':center_data})

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

def editarUsuario(request):
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
        password0 = request.POST["password0"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        job = request.POST["job"]
        degree = request.POST["degree"]
        bio = request.POST["bio"]

        try:
            usuario = User.objects.get(email=request.session['user_email'])
        except:
            response = redirect('login')
            return response
        
        if nombres != usuario.first_name:
            usuario.first_name = nombres
        if apellidos != usuario.last_name:
            usuario.last_name = apellidos
        if cedula != usuario.identity_card:
            usuario.identity_card = cedula
        if tel1 != usuario.phone_number_1:
            usuario.phone_number_1 = tel1
        if tel2 != usuario.phone_number_2:
            usuario.phone_number_2 = tel2
        if dir1 != usuario.direction.main_street:
            usuario.direction.main_street = dir1
        if dir2 != usuario.direction.secondary_street:
            usuario.direction.secondary_street = dir2
        if dir3 != usuario.direction.house_number:
            usuario.direction.house_number = dir3
        if dir4 != usuario.direction.reference:
            usuario.direction.reference = dir4
        if job != usuario.job_title:
            usuario.job_title = job
        if degree != usuario.degree:
            usuario.degree = degree
        if bio != usuario.biography:
            usuario.biography = bio
        if password0 == "" and password == "" and password2=="":
            usuario.save()
            """logout(request)
            request.session['user_email'] = usuario.email
            request.session['user_rol'] = usuario.rol"""

        elif password0 == usuario.password:
            if password == password2:
                usuario.password = password
                usuario.save()
            else:
                messages.success(request, 'Las contraseñas no coinciden')
                response = redirect('perfil')
                return response
        else:
            messages.success(request, 'Cambio de contraseña incorrecto')
            response = redirect('perfil')
            return response

        response = redirect('perfil')
        return response


def registrarPaciente(request):
    if request.method=="POST":
        nombres = request.POST["names"]
        apellidos = request.POST["lnames"]
        cedula = request.POST["id"]
        birth = request.POST["birth"]
        sex = request.POST["sex"]
        pais = request.POST["pais"]
        provincia = request.POST["provincia"]
        canton = request.POST["canton"]
        edu1 = request.POST["edu1"]
        edu2 = request.POST["edu2"]
        parroquia = request.POST["parroquia"]

        check1 = request.POST["check1"]
        check2 = request.POST["check2"]
        check3 = request.POST["check3"]
        check4 = request.POST["check4"]
        check5 = request.POST["check5"]

        image = request.POST["image"]

        relacion = request.POST["relacion"]

        tipoDiscapacidad = request.POST["discapacidad"]
        descripcionDiscapacidad = request.POST["descripcion"]
        porcentajeDiscapacidad = request.POST["porcentaje"]

        usuario = User.objects.get(email=request.session['user_email'])

        paciente = Patient(first_name=nombres, last_name=apellidos, identity_card=cedula, birth=birth, sex=sex, country_origin=pais, province=provincia, canton=canton, educational_institution_type=edu1, educational_institution=edu2, parish_type=parroquia, bond_desarrollo_humano=check1, bond_joaquin_gallegos=check2, alimony=check3, jubilee_pension=check4, montepio=check5, image=image)
        paciente.save()

        relacion = Relationship(representative=usuario, patient=paciente, relationship=relacion)
        relacion.save()

        discapacidad = Disability_card(patient=paciente, disability_type=tipoDiscapacidad, disability_description=descripcionDiscapacidad, disability_percentage=porcentajeDiscapacidad)
        discapacidad.save()

        subject="Registrar nuevo paciente"
        message= "Se requiere la aprobación del paciente de nombre" + " " + paciente.first_name + " " + paciente.last_name + ", con número de cédula " + paciente.identity_card + ", Su representante se llama: " + usuario.first_name + " " + usuario.last_name
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['alejo.sebas99@outlook.com']

        send_mail(subject, message, email_from, recipient_list)

        messages.success(request, 'Porfavor espera la respuesta en tu correo electrónico')
            

        #pacientes = Patient.objects.all()

        response = redirect('pacientes')
        return response


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
        del request.session['user_rol']
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

            messages.success(request, 'Porfavor espera la respuesta en tu correo electrónico')
            response = redirect('contact')
            return response
    
    return HttpResponse("Incorrecto")

def newEntry(request, email):
    user = User.objects.filter(email=email).first()
    if request.method=="POST":
        subject = request.POST["subject"]
        description = request.POST["description"]
        
        entry = Forum_entry(representative=user, subject=subject, description=description)
        entry.save()

        return redirect('/forum-entry.html/'+str(entry.id))
    else:
        return render(request, "index.html")

def comment(request, email, entry):
    en = Forum_entry.objects.filter(id=entry).first()
    user = User.objects.filter(email=email).first()
    if request.method=="POST":
        rp = request.POST["response"]
        
        res = Forum_response(entry=en, user=user, response=rp)
        res.save()

        return redirect('/forum-entry.html/'+str(entry))
    else:
        return render(request, "index.html")

def deleteComment(request, entry, id):
    response = Forum_response.objects.get(id=id)
    response.delete()
    return redirect('/forum-entry.html/'+str(entry))

def showForum(request, id):
    forum_responses = Forum_response.objects.filter(entry=id)
    entry = Forum_entry.objects.filter(id=id).first()
    entries = Forum_entry.objects.reverse()[:5].annotate(responses=Count('forum_response'))
    count_responses = Forum_response.objects.filter(entry=id).count()
    return render(request, 'forum-entry.html', {'center_data':center_data, 'entry':entry, 'responses':forum_responses, 'entries':entries, 'count_responses':count_responses})

def blogEntry(request, id):
    post = Post.objects.get(id=id)
    last_posts = Post.objects.reverse()[:5]
    return render(request, 'blog-entry.html', {'center_data':center_data, 'post':post, 'last_posts':last_posts})

def direction_list(request):
    direccion = Direction.objects.all()
    contexto = {'direcciones': direccion}
    return render(request, 'directory.html', contexto)

def directory_list(request):
    lugar = Directory.objects.all()
    contexto = {'directorios': lugar}
    return render(request, 'directory.html', contexto)