from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('app_2/', views.index),
    path('app_22/', views.index2)
]