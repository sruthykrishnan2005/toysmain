from django.urls import path
from .import views


urlpatterns = [
    path('',views.shop_login),
    
    #------------admin------------#
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    path('addproduct', views.addproduct),
    path('delete_product/<pid>',views.delete_product),
    path('view_bookings',views.view_bookings),

    
    #------------user--------------#
    path('register',views.register),
    path('user_home',views.user_home),
]

