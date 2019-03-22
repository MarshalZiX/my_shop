from django.views.generic.base import ContextMixin
# from shop.models import Category
from django.shortcuts import render, get_object_or_404
from shop.models import Product, Category
from cart.forms import CartAddProductForm


class HeaderContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update({
            'categories': Category.objects.all(),
        })
        return data

def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'common/header.html', {
        'category': category,
        'categories': categories,
        'products': products
    })