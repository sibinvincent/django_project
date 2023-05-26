from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('test/', views.test_fun),
    path('hom/', views.hom_fun),

]
