from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path('Register',views.Register),
    path('create_user',views.create_users),
    path('log',views.log),
    path('wall',views.walldisplay),
    path('logout',views.logout),
    path('create_post',views.create_post),
    path('create_comment/<int:i>',views.create_comment),
   # path('admin/', admin.site.urls),
]
