from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = (
        'order_number', 'date', 'delivery_cost', 'order_total', 'grand_total',
        'original_bag', 'stripe_pid',)

    fields = (
        'order_number', 'first_name', 'last_name', 'email', 'phone_number',
        'country', 'postcode', 'city', 'streetaddress', 'house_number',
        'date', 'delivery_cost', 'order_total', 'grand_total',
        'original_bag', 'stripe_pid',)

    list_display = (
        'order_number', 'date', 'first_name', 'last_name', 'email',
        'delivery_cost', 'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
