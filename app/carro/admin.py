from django.contrib import admin
from carro.models import Order, OrderItem
# Register your models here.
admin.site.register(Order),
admin.site.register(OrderItem)
