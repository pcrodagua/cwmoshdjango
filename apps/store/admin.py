from django.contrib import admin, messages
from django.db.models import Count, QuerySet
from django.utils.html import format_html, urlencode
from apps.store.models import Product, Customer, Order, Collection
from django.urls import reverse

from apps.tags.models import TaggedItem


class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'By inventory'

    def lookups(self, request, model_admin):
        return [
            ("<10", "Low"),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


class TagInline(admin.TabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # inlines = [TagInline]
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        "slug": ("title",)
    }
    exclude = ["promotions"]
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price", ]
    list_select_related = ["collection"]
    list_filter = ["collection", "last_update", InventoryFilter]
    list_per_page = 50
    actions = ["clear_inventory"]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory <= 10:
            return "LOW"
        return "OK"

    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset: QuerySet):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, f'{updated_count} products where succesfully updated.',
            messages.ERROR
        )


# TODO: Add a new column for viewing the orders of each customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "membership", "orders_counts"]
    list_editable = ["last_name", "phone"]
    list_display_links = ("first_name",)
    list_filter = ["order"]  # Assuming there is a ForeignKey named 'order' in Customer model
    ordering = ["first_name", "last_name"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]
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
    search_fields = ["title"]

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
