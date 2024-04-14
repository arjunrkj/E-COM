from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name = 'orders')
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    total_price = models.FloatField(default=0)
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSING = 2
    ORDER_PROCESSED = 3
    ORDER_DELIVERED = 4
    ORDER_REJECTED = 5
    STATUS_CHOICE = ((ORDER_PROCESSING,"ORDER_PROCESSING"),
                     (ORDER_PROCESSING,"ORDER_PROCESSED"),
                     (ORDER_DELIVERED,"ORDER_DELIVERED"),
                     (ORDER_REJECTED,"ORDER_REJECTED"))
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "order--{}--{}".format(self.id,self.owner.user.username)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='added_carts', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')
    size = models.CharField(max_length=10,default='L')