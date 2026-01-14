from django.urls import path
from .views import index, client, about,products,contact,detail,ProductsCreate
urlpatterns = [
    path('', index, name='index'),
    path('client/', client, name='client'  ),
    path('about/', about, name='haqida' ),
    path('products/', products, name='products' ),
    path('contact/', contact, name='contact' ),
    path('detail/<int:id>/', detail, name='detail'),
    path('products/create/', ProductsCreate.as_view(), name='create')
]