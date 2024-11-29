from django.urls import path
from .import views


urlpatterns = [
    path('',views.shop_login),
    
    #------------admin------------#
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    
    #------------user--------------#
    path('register',views.register),
    path('user_home',views.user_home),
]

