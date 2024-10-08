from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category
from . models import Product
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.db.models import Q



# this function work for pagination and show all the product in store page. 
def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': page_product,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


# this function work for show the details of the products.
def product_detail(request, category_slug, product_slug):
    try:
        # making url (store/category_slug/product_slug)
        products = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),  product=products).exists()
    except Exception as e:
        raise e
    context = {
        'product': products,
        'in_cart': in_cart,
    }
    return render(request, 'store/product-detail.html', context)


# this function work for search the products.
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )
            product_count = products.count()
        context = {
            'products': products,
            'product_count': product_count,
        }
    return render(request, 'store/store.html',context)