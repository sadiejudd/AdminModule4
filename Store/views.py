from django.shortcuts import render
from .models import Product
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def Products(request):
    template = loader.get_template('Store/products.html')
    products = Product.objects.all()
    context = {
        'products': products


    }

    return HttpResponse(template.render(context, request))


