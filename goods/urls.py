from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
  path('search/', views.catalog, name='search'),
  path('<slug:cat_slug>/', views.catalog, name='index'),
  # path('<slug:cat_slug>/', views.catalog, name='category'),
  path('product/<slug:slug>/', views.product, name='product'),
]