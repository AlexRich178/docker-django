from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all().order_by('price')
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        phones = Phone.objects.all().order_by('name')
    if sort_by == 'min_price':
        phones = Phone.objects.all().order_by('price')
    if sort_by == "max_price":
        phones = Phone.objects.all().order_by('-price')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {
        'phone': phone
    }
    return render(request, template, context)
