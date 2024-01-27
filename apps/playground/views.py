from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F, Count, Min, Max, Avg, Sum
from apps.store.models import Product, Customer, Collection, Order, OrderItem


# def say_hello(request):
#     queryset = Product.objects.all()  # returns a queryset
#     product = Product.objects.get(pk=1)  # returns the element matching the actual object not a queryset
#     # try:
#     #     product = Product.objects.get(pk=0)  # if element doest not exist it will raise an exception
#     # except ObjectDoesNotExist:
#     #     return HttpResponse("Product does not exist")
#     # this returns none
#     product = Product.objects.filter(pk=0).first()
#     # this returns a bool
#     product_exists = Product.objects.filter(pk=0).exists()
#
#     # filter all products that cost $20
#     queryset = Product.objects.filter(unit_price__range=(20, 30), title__icontains='coffee')
#
#     # Customers with .com accounts
#     queryset = Customer.objects.filter(email__endswith='.com')
#     # •Collections that don’t have a featured product
#     queryset = Collection.objects.filter(featured_product__isnull=True)
#     # •Products with low inventory (less than 10)
#     queryset = Product.objects.filter(inventory__lt=10)
#     # •Orders placed by customer with id = 1
#     queryset = Order.objects.filter(customer__id=1)
#     # •Order items for products in collection 3
#     queryset = OrderItem.objects.filter(product__colection=3)
#
#     return render(request, 'hello.html', context={'name': 'Pablo', 'products': list(queryset)})


# def say_hello(request):
#     # queryset = OrderItem.objects.values("product__id").distinct()
#     # products = Product.objects.filter(id__in=queryset).values('id', 'title', 'unit_price')
#
#     # using only
#     queryset = Product.objects.only('id', 'title')
#
#     # using defer
#     queryset = Product.objects.defer('id', 'title')
#
#     return render(request, 'hello.html', context={'name': 'Pablo', 'products': list(products)})


# def say_hello(request):
#     #  select_related for (1)
#     queryset = Product.objects.select_related('collection').all()
#     #  prefetch_related for (*)
#     queryset = Product.objects.prefetch_related('collection').all()
#     return render(request, 'hello.html', context={'name': 'Pablo', 'products': list(products)})


# def say_hello(request):
#     # aggregating and annotating objects
#     queryset = Product.objects.aggregate(
#         count=Count('id'),
#         min_price=Min('unit_price'),
#         max_price=Max('unit_price')
#     )
#
#     # how many orders do we have
#     queryset = Order.objects.aggregate(count=Count('id'))
#     # how many units of product 1 have we sold
#     queryset = OrderItem.objects.filter(product__id=1).aggregate(
#         count=Sum('quantity')
#     )
#     # how many orders has customer 1 placed
#     queryset = Order.objects.filter(customer__id=1).aggregate(
#         count=Count('id')
#     )
#     # what is the min, max and average price of the products collection 3?
#     queryset = Product.objects.filter(collection__id=3).aggregate(
#         min_price=Min('unit_price'),
#         max_price=Max('unit_price'),
#         average=Avg('unit_price')
#     )
#     return render(request, 'hello.html', context={'name': 'Pablo', 'products': list(products)})

def say_hello(request):
    return render(request, 'hello.html', context={'name': 'Pablo', 'products': list(products)})
