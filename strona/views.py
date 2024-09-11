from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'strona/home.html', {'products':products})







