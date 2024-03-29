from django.shortcuts import get_object_or_404, render
from goods.models import Products


def catalog(request, cat_slug=None):
  if cat_slug == 'vse-tovary':
    goods = Products.objects.all()
  else:
    goods = get_object_or_404(Products.objects.filter(category__slug=cat_slug))

  context = {
    'title': 'Home catalog',
    'goods': goods,
  }
  
  return render(request, 'goods/catalog.html', context)


def product(request, slug):
  product = Products.objects.get(slug=slug)
  
  context = {
    'product': product
  }

  return render(request, 'goods/product.html', context=context)
