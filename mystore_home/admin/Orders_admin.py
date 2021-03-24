from django.contrib import admin
from mystore_home.models import Shipping_Address, Order, Payment, Order_Detail

admin.site.register(Shipping_Address)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Order_Detail)