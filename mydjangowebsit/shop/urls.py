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
    path("handlerequest/",views.handleRequest,name='handlerequest'),
    path("bat/",views.bat,name='bat'),
    path("gloves/",views.gloves,name='gloves'),
    path("helmets/",views.helmets,name='helmets'),
    path("balls/",views.balls,name='balls'),
    path("pads/",views.pads,name='pads')
    
]
