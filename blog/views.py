from django.shortcuts import render
from django.template.defaultfilters import title

from .models import Beauty,Products
# Create your views here.
def index(request):
    title = "Home"
    beauty = Beauty.objects.all()
    products = Products.objects.all()
    malumot = {
        "title": title,
        "beauty": beauty,
        'products':products
    }
    return render(request, 'index.html', context=malumot)

def client(request):
    title = "Client"
    return render(request, 'client.html',context={"title": title})

def about(request):
    title = "About"
    return render(request, 'about.html',context={"title": title})

def contact(request):
    title = "Contact"
    return render(request, 'contact.html',context={"title": title})

def products(request):
    title = "Products"
    products = Products.objects.all()
    malumot = {
        "title": title,
        'products': products
    }
    return render(request, 'products.html',context=malumot)


def detail(request,id):
    title = 'detail'
    product = Products.objects.get(id=id)
    return render(request, 'detail.html', context={'title':title, 'p':product})