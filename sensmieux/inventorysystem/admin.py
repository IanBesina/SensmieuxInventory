from django.contrib import admin
from inventorysystem.models import Product, Stock, Invoice, Invoice_Item
# Register your models here.
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Invoice)
admin.site.register(Invoice_Item)
