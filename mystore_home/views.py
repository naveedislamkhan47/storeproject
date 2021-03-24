from django.shortcuts import render
from django.http import HttpResponse
from mystore_home.models import Product
# Create your views here.
def home(request):
    return render(request, 'mystore_home/homepage.html')

def products(request):
    all_products = Product.objects.all()
    context = {
        'products' : all_products
    }
    return render(request, 'mystore_home/products.html', context)