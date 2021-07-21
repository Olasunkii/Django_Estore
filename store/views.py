from django.shortcuts import render, get_object_or_404
from .models import Category, Product


#View all products in the home page
def all_products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'store/home.html', context)

#This function selects products according to their categories from navbar
def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 
    'products': products}
    return render(request, 'store/products/category.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})