from django.urls import path
from .import views


urlpatterns = [
    path('',views.shop_login),
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
]