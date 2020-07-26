from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blogsingle, name='blogsingle'),
    path('contact.html', views.contact, name='contact'),
    path('courses.html', views.courses, name='courses'),
    path('pricing.html', views.pricing, name='pricing'),
    path('teacher.html', views.teacher, name='teacher'),
]