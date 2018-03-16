from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()[:10]
    context = {
        'title':'Currently Sold Out.',
        'Product':products
    }

    return render(request, 'Product/index.html', context)


def product_details(request, id):
    product = Product.objects.get(id=id)
    context = {
        'Product':product
    }
    
    return render(request, 'Product/product_details.html', context)