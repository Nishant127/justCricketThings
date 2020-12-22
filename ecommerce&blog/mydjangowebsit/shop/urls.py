from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index,name='homeShop'),
    path("about/",views.about,name='about'),
    path("contactus/",views.contactUs,name='contactus'),
    path("productview/",views.productView,name='productview'),
    path("search/",views.search,name='search'),
    path("tracker/",views.tracker,name='tracker'),
    path("checkout/",views.checkout,name='checkout')
    
    
]
