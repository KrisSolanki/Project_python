from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display_users/', views.display_users, name='display_users'),
    #  path('user_form/', views.user_form, name='user_form'),  # Add this line

]