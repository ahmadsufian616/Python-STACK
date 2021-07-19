from django.contrib import admin
from django.urls import path
from . import views
import show
urlpatterns = [
    path('shows/',views.showall),
    path('shows/new',views.Addnewshow),
    path('shows/<int:i>',views.show),
    path('shows/<int:i>/edit',views.edit),
    path('shows/<int:i>/update',views.update),
    path('shows/<int:i>/delete',views.delete),
    path('shows/addshow',views.create),
    
]