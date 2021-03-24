from django.db import models
from mystore_users.models import User
from phonenumber_field.modelfields import PhoneNumberField
################################################## Customer Models ##########################################################

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, blank = True, null = True)
    first_name = models.CharField(max_length = 150, null = True)
    last_name = models.CharField(max_length = 150, null = True)
    email = models.EmailField(max_length=254, null = True, verbose_name='email address')
    phone = PhoneNumberField()
    
    def __str__(self): 
        return f'{self.first_name}'
