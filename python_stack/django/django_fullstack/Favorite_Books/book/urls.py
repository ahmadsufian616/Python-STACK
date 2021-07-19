from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('create_user',views.create_user),
    path('logs',views.logs),
    path('book',views.book),
    path('addbook',views.addbook),
    path('bookdesc/<int:i>',views.bookdesc),
    path('editbook/<int:i>',views.edit),
    path('logout',views.logout),
    path('like_book/<int:i>',views.like_book),
    #path('admin/', admin.site.urls),
    
]