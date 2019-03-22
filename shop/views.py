from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
# Страница с товарами


def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    print(request.POST)

    try:
        _from = int(request.POST.get('from'))
    except (ValueError, TypeError):
        _from = None

    try:
        to = int(request.POST.get('to'))
    except (ValueError, TypeError):
        to = None

    if _from and to:
        products = Product.objects.filter(available=True, price__gte=_from, price__lte=to)
    elif _from:
        products = Product.objects.filter(available=True, price__gte=_from)
    elif to:
        products = Product.objects.filter(available=True, price__lte=to)
    else:
        products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'to': to or '',
        'from': _from or '',
    })

def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form,
                              'categories': Category.objects.all()})
# Create your views here.
