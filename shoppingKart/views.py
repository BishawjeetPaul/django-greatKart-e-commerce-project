from django.shortcuts import render
from store.models import Product


# this function work for website homepage and show all the product in the homepage.
def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)