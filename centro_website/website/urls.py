from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('forum.html', views.forum, name='forum'),
    path('forum-entry.html', views.forumEntry, name='forum-entry'),
    path('contact.html', views.contact, name='contact'),

    path('donations.html', views.donations, name='donations'),
    path('index.html', views.index, name='index'),
    path('information.html', views.information, name='information'),
    path('login.html', views.login, name='login'),
    path('pacientes.html', views.pacientes, name='pacientes'),
    path('registro.html', views.registro, name='registro'),
    path('registro-paciente.html', views.registroPaciente, name='registroPaciente'),
    path('report.html', views.report, name='report'),
    path('therapies.html', views.therapies, name='therapies'),
    path('blog.html', views.blog, name='blog'),
    path('training.html', views.training, name='training'),
    path('tutorial.html', views.tutorial, name='tutorial'),
    path('disabilities.html', views.disabilities, name='disabilities'),
    path('directory.html', views.directory, name='directory'),

    path('registrar/', views.registrar),
    path('iniciarSesion/', views.iniciarSesion),
    path('logout/', views.logout),
    path('enviarCorreo/', views.enviarCorreo),
    path('forum-entry.html/<int:id>', views.showForum),
    path('blog-entry.html/<int:id>', views.blogEntry),
    path('comment/<str:email>/<int:entry>', views.comment),
    path('registrarPaciente/', views.registrarPaciente),
    path('delete-comment/<int:entry>/<int:id>', views.deleteComment),
    path('new-entry/<str:email>', views.newEntry),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

