from users.models import Account
from django.db import models
from productos.models import productos


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='orders')
    first_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    place = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=3,blank=True)
    stripe_token = models.CharField(max_length=150)

    class Meta:
        ordering = ['created_at',]

    def __str__(self):
        return self.place

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(productos, related_name='items', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.order