from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index,name='homeShop'),
    path("aboutUs/",views.about,name='about'),
    path("contactUs/",views.contactUs,name='contactus'),
    path("products/<int:myid>",views.productView,name='productview'),
    path("search/",views.search,name='search'),
    path("tracker/",views.tracker,name='tracker'),
    path("checkout/",views.checkout,name='checkout'),
    path("handlerequest/",views.handleRequest,name='handlerequest')
    
    
]
