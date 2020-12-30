from django.urls import path
from .views import register,index,u_login,u_logout
app_name= 'userapp'
urlpatterns =[path('',index,name='index'),
              path('register/',register,name="register"),
              path('login/',u_login,name='login' ),
              path('logout/',u_logout,name='logout'),]