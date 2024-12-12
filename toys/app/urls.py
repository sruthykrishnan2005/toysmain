from django.urls import path
from .import views
from .views import category_view

urlpatterns = [
    path('',views.shop_login),
    
    #------------admin------------#
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    path('addproduct', views.addproduct),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),
    path('view_bookings',views.view_bookings),
    
    
    #------------user--------------#
    path('register',views.register),
    path('user_home',views.user_home),
    path('contact/', views.contact),
    path('about_us', views.about_us),
    path('view_product/<pid>',views.view_product),
    path('category/', category_view),

]

