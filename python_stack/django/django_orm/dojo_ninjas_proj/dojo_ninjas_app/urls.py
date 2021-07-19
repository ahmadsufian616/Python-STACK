from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun),
    path('dojo',views.fun2),
    path('ninja',views.fun3),
]
