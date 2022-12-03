from django.contrib import admin
from django.urls import path
from room.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('user_home',user_home,name='user_home'),
    path('Logout',Logout,name='Logout'),
    path('admin_home',admin_home,name='admin_home'),
    path('view_user',view_user,name='view_user'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    path('add_room',add_room,name='add_room'),
    path('view_room_user',view_room_user,name='view_room_user'),
    path('view_room_admin',view_room_admin,name='view_room_admin'),
    path('edit_room',edit_room,name='edit_room'),
    path('info',info,name='info')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
