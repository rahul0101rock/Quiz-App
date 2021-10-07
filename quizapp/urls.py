from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    re_path(r'^(?P<choice>[\w]+)', views.questions, name='questions'),

]