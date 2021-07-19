from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.fun),
    path('process_money',views.process_money),
    path('reset',views.reset),
    
    
]