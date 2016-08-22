from django.http import Http404
from django.shortcuts import render

# Create your views here.
from products.models import Product, ProductImage


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__contains=q)
        context = {'query': q, 'products': products}
        template = 'products/result.html'
    else:
        template = 'products/home.html'
        context = {}
    return render(request, template, context)


def home(request):
    products = Product.objects.all()
    template = 'products/home.html'
    context = {"products": products}
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {"products": products}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        # images = product.productimage_set.all()
        images = ProductImage.objects.filter(product=product)

        print product.title
        context = {"product": product, "images": images}
        template = 'products/single.html'
        return render(request, template, context)

    except:
        raise Http404
