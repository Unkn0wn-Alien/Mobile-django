from django.shortcuts import render
from .models import *

def get_brands(request):
    queryset = Brand.objects.all().order_by('brand_name')
    return render(request, 'index.html', {'brand' : queryset})

def get_models(request, madel_id):
    queryset = Madel.objects.all().filter(brand=madel_id)
    brand = Brand.objects.get(brand_id=madel_id)
    contex = {'model' : queryset, 'brand' : brand}
    return render(request, 'models.html', contex)

def get_products(request, product_id):
    queryset = Product.objects.all().filter(product_madel=product_id)
    model = Madel.objects.get(madel_id=product_id)
    brand = Brand.objects.get(brand_id=product_id)
    contex = {'product' : queryset, 'model' : model, 'brand' : brand}
    return render(request, 'products.html', contex)