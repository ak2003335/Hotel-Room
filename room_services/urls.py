from django.contrib import admin
from django.urls import path
from room.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('signin',login,name='signin'),
    path('signup',signup,name='signup'),
    path('user_home',user_home,name='user_home'),
    path('Logout',Logout,name='Logout'),
    path('admin_home',admin_home,name='admin_home'),
    path('view_user',view_user,name='view_user'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)