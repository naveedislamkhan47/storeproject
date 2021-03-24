from django.db import models
from .Customers import Customer
from .Shippers import Shipper
from .Products import Product_Detail
from django_countries.fields import CountryField
################################ Models for Order and Payments (Order, OrderDetails, Payments) ##############################

class Payment(models.Model):
    payment_choices = [
        ('CR', 'Credit Card'),
        ('DR', 'Debit Card'),
        ('COD', 'Cash On Delivery')
    ]
    payment_method = models.CharField(choices = payment_choices, max_length = 3)

    def __str__(self):
        return f"{self.payment_method}"


class Order(models.Model):
    shipper = models.ForeignKey(Shipper, on_delete = models.SET_NULL, null = True, blank = True)
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True, blank = False)
    payment = models.ForeignKey(Payment, on_delete = models.SET_NULL, null = True, blank = False)
    date_ordered = models.DateTimeField(auto_now_add = True)
    fullfilled = models.BooleanField(default = False, blank = False)
    status = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.id}'


class Shipping_Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null = True)
    address = models.CharField(max_length = 250)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 100)
    country = CountryField()
    date_joined = models.DateTimeField(auto_now_add = True)


class Order_Detail(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, null = True, blank = True)
    product_detail = models.ForeignKey(Product_Detail, on_delete = models.SET_NULL, null = True, blank = True)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Order #{self.order.id}, CustomerName = {self.order.customer.first_name + self.order.customer.last_name}'