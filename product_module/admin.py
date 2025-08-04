from django.contrib import admin
from . import models


def formatted_price(obj):
    return f"{obj.price:,}"


formatted_price.short_description = "Price"


class ProductAdmin(admin.ModelAdmin):
    list_filter = ["title", "category", "is_active", "brand"]
    # list_editable = ['title', 'price','is_active']
    list_display = ["title", "price", "is_active", "is_delete", formatted_price]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductGallery)
# admin.site.register(models.Product_active)
