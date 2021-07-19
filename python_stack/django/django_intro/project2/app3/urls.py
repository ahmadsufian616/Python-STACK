from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('app_3/', views.i),
    path('app_32/', views.i2)
]