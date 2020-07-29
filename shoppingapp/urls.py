
from django.contrib import admin
from django.urls import path
from shoppingapp import views as v

urlpatterns = [
    path('',v.index),
    path('addUser',v.addUser),
    path('Login',v.Login),
    path('getProduct',v.getProduct),
    path('searchProduct',v.searchProduct),
    path('Logout',v.Logout),
    path('productList',v.productList),
    path('addToCart',v.addToCart),
    path('cartList',v.cartList),
    path('editProfile',v.editProfile),
    path('myorder',v.myorder),
    path('imagedata',v.imagedata),
    
]
