from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Contact, Order
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum 
from django.http import HttpResponse

MERCHANT_KEY = 'cuC3sG9G8JkpHqa&'
def index(request):
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
    if request.method=='POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

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
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount','')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Order(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        thank=True
        id=order.order_id
        param_dict={

        'MID': 'dayPrl28492702568848',
        'ORDER_ID': str(order.order_id),
        'TXN_AMOUNT': str(amount),
        'CUST_ID': 'email',
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
         }
        param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request, 'shop/paytm.html',{'param_dict':param_dict})
    return render(request, 'shop/checkout.html')

@csrf_exempt
def handleRequest(request):
    form=request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i]=form[i]
        if i=='CHECKSUMHASH':
            checksum=form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
            print('ORDER SUCCESFUL')
        else :
            print('order was not successful because' + response_dict['RESPMSG'])            
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})
