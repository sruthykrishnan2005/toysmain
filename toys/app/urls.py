from django.urls import path
from .import views


urlpatterns = [
    path('',views.shop_login),
    
    #------------admin------------#
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    path('addproduct', views.addproduct),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),
    path('add_cate',views.add_category),
    path('view_bookings',views.view_bookings),
    
    
    #------------user--------------#
    path('register',views.register),
    path('user_home',views.user_home),
    path('contact/', views.contact),
    path('about_us', views.about_us),
    path('product_view/<pid>',views.product_view),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('cart_pro_buy/<cid>',views.cart_pro_buy),
    path('bookings',views.bookings),
    path('pro_buy/<pid>',views.pro_buy),
    path('qty_in/<cid>',views.qty_in),
    path('qty_dec/<cid>',views.qty_dec),
    path('ride-on-vehicles/<int:name>/', views.ride_on_vehicles),



]

