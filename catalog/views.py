from gc import get_objects

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product

from catalog.models import Product


# Create your views here.


def products_list(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "catalog/products_list.html", context)


def contacts(request):
    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    product = get_object_or_404 (Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)