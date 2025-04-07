from django.urls import path   
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('python',views.python,name='python'),
    path('java',views.java,name='java'),
    path('c',views.c,name='c'),
    path('cpp',views.cpp,name='cpp'),
    path('react',views.react,name='react'),
    path('maths',views.maths,name='maths'),
    path('contact',views.contact,name='contact'),




]
