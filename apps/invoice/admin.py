from django.contrib import admin

from .models import Order, OrderDetail, Invoice

class OrderDetailInline(admin.TabularInline):
    '''Tabular Inline View for OrderDetail'''

    model = OrderDetail
    extra =0


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    '''Admin View for Invoice'''

    list_display = ('invoice_number','customer', 'order','date','total', 'payment')
    ordering = ('invoice_number','date',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ['id', 'date', 'status', 'total' ]
    inlines = [OrderDetailInline]