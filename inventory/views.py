from itertools import product
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import *

#Product

def list_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product.html', {'products':products, 'categories':categories})

"""
class detail_product(TemplateView):
    template_name = 'detail.html'
"""

def detail_product(request, id):
    product = Product.objects.get(id=id)
    product_tags = product.tags.all()
    tags = Tag.objects.all()
    return render(request, 'detail.html', {'product':product, 'product_tags':product_tags, 'tags':tags})

def add_tag(request, id):
    tag_id = request.POST['tag_id']
    tag = Tag.objects.get(id=tag_id)
    product = Product.objects.get(id=id)
    product.tags.add(tag)
    return redirect(f'/detalle/producto/{product.id}')

def remove_tag(request, id):
    tag_id = request.POST['tag_id']
    tag = Tag.objects.get(id=tag_id)
    product = Product.objects.get(id=id)
    product.tags.remove(tag)
    return redirect(f'/detalle/producto/{product.id}')

def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        stock = request.POST['stock']
        price = request.POST['price']
        category_id = request.POST['category_id']
        category = Category.objects.get(id=category_id)
        product = Product(name=name, stock=stock, price=price, category=category)
        product.save()
        return redirect('/')
    else:
        return redirect('/')

def update_product(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        name = request.POST['name']
        stock = request.POST['stock']
        price = request.POST['price']
        category_id = request.POST['category_id']
        category = Category.objects.get(id=category_id)
        product.name = name
        product.stock = stock
        product.price = price
        product.category = category
        product.save()
        return redirect('/')
    else:
        return redirect('/')

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')

#Category

class ListCategories(ListView):
    model = Category
    template_name = 'category.html'

class CreateCategory(CreateView):
    model = Category
    fields = ['name']
    success_url = '/categorias/'

class UpdateCategory(UpdateView):
    model = Category
    fields = ['name']
    success_url = '/categorias/'

"""
class DeleteCategory(DeleteView):
    model = Category
    success_url = '/categorias/'
"""
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/categorias/')

#Sale

def list_sales(request):
    sales = Sale.objects.all()
    products = Product.objects.all()
    return render(request, 'sale.html', {'sales':sales, 'products':products})

def process_sale(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        product = Product.objects.get(id=product_id)
        detail = request.POST['detail']
        quanty = int(request.POST['quanty'])
        product.stock -= quanty
        total = product.price * quanty
        sale = Sale(detail=detail, quanty=quanty, total=total, product=product)
        product.save()
        sale.save()
        return redirect('/ventas/')