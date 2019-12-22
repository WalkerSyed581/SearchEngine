from django.urls import path

from . import views

app_name = 'myEngine'

urlpatterns = [

    path('', views.index, name='index'),

]