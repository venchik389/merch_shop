from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_id=None):
    category = None
    products = Product.objects.all()
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    return render(request, 'shop/product_list.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})
