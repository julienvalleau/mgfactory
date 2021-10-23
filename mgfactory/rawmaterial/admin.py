from django.contrib import admin

from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['country', 'province', 'state']