from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blogsingle, name='blogsingle'),
    path('contact.html', views.contact, name='contact'),
    path('directory.html', views.directory, name='directory'),
    path('donations.html', views.donations, name='donations'),
    path('index.html', views.index, name='index'),
    path('information.html', views.information, name='information'),
    path('login.html', views.login, name='login'),
    path('registro.html', views.registro, name='registro'),
    path('report.html', views.report, name='report'),
    path('therapies.html', views.therapies, name='therapies'),
    path('tips.html', views.tips, name='tips'),
    path('training.html', views.training, name='training'),
    path('tutorial.html', views.tutorial, name='tutorial'),

    path('registrar/', views.registrar),
    path('iniciarSesion/', views.iniciarSesion),
    path('logout/', views.logout),
]