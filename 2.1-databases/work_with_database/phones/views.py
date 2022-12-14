from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    if sort == 'min_price':
        context = {'phones': Phone.objects.all().order_by('price')}
    elif sort == 'max_price':
        context = {'phones': Phone.objects.all().order_by('-price')}
    elif sort == 'name':
        context = {'phones': Phone.objects.all().order_by('name')}
    else:
        context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug).first}
    return render(request, template, context)
