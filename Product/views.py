from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):

    print('Welcome home')
    products = Product.objects.all()[:10]
    context = {
        'Product':products
    }

    return render(request, 'Product/index.html', context)


def product_details(request, id):
    product = Product.objects.all()
    context = {
        'current_product': Product.objects.get(id=id),
        'Product':product
    }
    
    return render(request, 'Product/product_details.html', context)

def Category(request, category):
    #print(category)
    product = Product.objects.all().filter(category=category)
    print("<<LLLL<<: "+str(product))
    context = {
        'Product':product
    }
    print(context)
    return render(request, 'Product/index.html', context)