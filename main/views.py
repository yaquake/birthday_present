from django.shortcuts import render, redirect
from .models import Painting
from django.core.paginator import Paginator

numbers = {
    '1': 'Ena',
    '2': 'Dio',
    '3': 'Tria',
    '4': 'Tessera',
    '5': 'Pente',
    '6': 'Exi',
    '7': 'Epta',
    '8': 'Octo',
    '9': 'Ennea',
    '10': 'Deka'
}


def home(request):
    return redirect('pages', page=1)


def pages(request, page):
    paintings = Painting.objects.all().order_by('pk')
    paginator = Paginator(paintings, 9)
    result = paginator.page(page)
    return render(request, 'index.html', {'paintings': result})
