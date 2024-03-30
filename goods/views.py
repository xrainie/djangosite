from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from goods.models import Products


def catalog(request, cat_slug=None, page=1):
  if cat_slug == 'vse-tovary':
    goods = Products.objects.all()
  else:
    goods = get_list_or_404(Products.objects.filter(category__slug=cat_slug))

  paginator = Paginator(goods, 3, allow_empty_first_page=False)
  current_page = paginator.page(page)

  context = {
    'title': 'Home catalog',
    'goods': current_page,
    'slug_url': cat_slug
  }
  
  return render(request, 'goods/catalog.html', context)


def product(request, slug):
  product = Products.objects.get(slug=slug)
  
  context = {
    'product': product
  }

  return render(request, 'goods/product.html', context=context)
