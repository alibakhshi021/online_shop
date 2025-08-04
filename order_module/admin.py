from django.contrib import admin
from django.contrib.admin import site

from order_module import models
from order_module.models import Order

# Register your models here.

admin.site.register(models.Order)
admin.site.register(models.OrderDetail)
