from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  context = {
    'title': 'Home - Главная',
    'content': 'Магазин мебели HOME',
    'footer': 'Copyright &copy; Home Python Hub Studio 2023'
  }
  return render(request, 'main/index.html', context=context)


def about(request):
  context = {
    'title': 'Home - О нас',
    'content': 'Магазин мебели HOME',
    'footer': 'Copyright &copy; Home Python Hub Studio 2023',
    'text_on_page': 'Какой крутой магазин у нас, покупайте, наслаждайтесь!'
  }
  return render(request, 'main/about.html', context=context)
