from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from apps.store.models import Product, Customer, Order, Collection
from django.urls import reverse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price", ]
    list_select_related = ["collection"]
    list_filter = ["collection"]
    list_per_page = 50

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory <= 10:
            return "LOW"
        return "OK"


# TODO: Add a new column for viewing the orders of each customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "membership", "orders_counts"]
    list_editable = ["last_name", "phone"]
    list_display_links = ("first_name",)
    list_filter = ["order"]  # Assuming there is a ForeignKey named 'order' in Customer model
    ordering = ["first_name", "last_name"]
    list_per_page = 50

    @admin.display(ordering="orders_counts")
    def orders_counts(self, customer):
        url = reverse(
            "admin:store_order_changelist"
        ) + "?" + urlencode({
            "customer__id": str(customer.id)
        })
        return format_html(f'<a href="{url}">{customer.orders_counts}</a>')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_counts=Count("order")
        )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    list_filter = ["customer"]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_counts"]

    @admin.display(ordering="products_counts")
    def products_counts(self, collection):
        url = reverse(
            viewname="admin:store_product_changelist",
        ) + "?" + urlencode({
            "collection__id": str(collection.id)
        })
        return format_html(
            format_string=f'<a href="{url}">{collection.products_counts}</a>',
        )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_counts=Count("product")
        )
