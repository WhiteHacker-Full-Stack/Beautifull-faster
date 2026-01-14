from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.defaultfilters import title
from django.views.generic import CreateView,UpdateView,DeleteView
from user.models import Izoh

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

@login_required(login_url='/user/login/')
def detail(request,id):
    user = request.user
    title = 'detail'
    product = Products.objects.get(id=id)
    izohlar = Izoh.objects.filter(product=product)
    if request.method == 'POST':
        text = request.POST['text']
        izoh = Izoh.objects.create(text=text, product=product,user=user)
    return render(request, 'detail.html', context={'title':title, 'p':product, 'izohlar':izohlar})

class ProductsCreate(CreateView):
    model = Products
    template_name = 'crud/create.html'
    success_url = '/'
    fields = ['name', 'text', 'img', 'price']
