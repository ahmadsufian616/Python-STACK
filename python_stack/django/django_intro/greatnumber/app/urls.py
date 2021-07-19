#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fun),
    path('test',views.fun2),
    path('del',views.fun3),
]
