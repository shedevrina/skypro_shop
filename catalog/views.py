from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

from catalog.models import Product


# Create your views here.


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")


def product_details(request):
    return render(request, "catalog/product_details.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)
