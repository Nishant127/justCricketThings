from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

def index(request):
    # products = Product.objects.all()
    # print(products)

    # # params = {'product':products, 'no_of_slides':nSlides, 'range':range(1,nSlides)}
    # allProds = [[products ,range(1,nSlides) ,nSlides],
    #             [products ,range(1,nSlides) ,nSlides]]
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = { item['category'] for item in catProds }
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = (n//4) - ceil((n/4) - (n//4))
        allProds.append([ prod ,range(1,nSlides) ,nSlides])
    params={'allProds':allProds}            
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contactUs(request):
    return render(request,'shop/contactUs.html')

def productView(request,myid):
    product = Product.objects.filter(id=myid)

    print(product)
    return render(request,'shop/productView.html',{'product':product[0]})

def search(request):
    return HttpResponse('We are at search')

def tracker(request):
    return render(request,'shop/tracker.html')

def checkout(request):
    return HttpResponse('We are at checkout')