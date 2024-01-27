from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F
from apps.store.models import Product, Customer, Collection, Order, OrderItem


def say_hello(request):
    queryset = Product.objects.all()  # returns a queryset
    product = Product.objects.get(pk=1)  # returns the element matching the actual object not a queryset
    # try:
    #     product = Product.objects.get(pk=0)  # if element doest not exist it will raise an exception
    # except ObjectDoesNotExist:
    #     return HttpResponse("Product does not exist")
    # this returns none
    product = Product.objects.filter(pk=0).first()
    # this returns a bool
    product_exists = Product.objects.filter(pk=0).exists()

    # filter all products that cost $20
    queryset = Product.objects.filter(unit_price__range=(20, 30), title__icontains='coffee')

    # Customers with .com accounts
    queryset = Customer.objects.filter(email__endswith='.com')
    # •Collections that don’t have a featured product
    queryset = Collection.objects.filter(featured_product__isnull=True)
    # •Products with low inventory (less than 10)
    queryset = Product.objects.filter(inventory__lt=10)
    # •Orders placed by customer with id = 1
    queryset = Order.objects.filter(customer__id=1)
    # •Order items for products in collection 3
    queryset = OrderItem.objects.filter(product__colection=3)

    return render(request, 'hello.html', context={'name': 'Pablo', 'products': list(queryset)})


def say_hello(request):
    queryset = Product.objects.filter(
        Q(inventory__lt=10) | Q(unit_price__lt=20)
    )
    return render(request, 'hello.html', context={'name': 'Pablo', 'products': list(queryset)})
