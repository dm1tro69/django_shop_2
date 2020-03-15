from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product

# Create your views here.

class ProductsList(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = 'shop/list_product.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/list_detail.html'
    context_object_name = 'list_detail'

