from typing import Dict


from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.fun),
    path('authers', views.fun2),
    path('Add-Book',views.ADDBOOK),
    path('Add-Auther',views.ADDAUTHERS),
    path('viewbook',views.viewbook),
    path('viewaruther',views.viewaurther),
    path('assignBook',views.assignBook),
    path('assignaurther',views.assignaurther),
  
]
