from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display_users/', views.display_users, name='display_users'),
    

]