from django.db import models

##################################### Models for the Suppliers of a Product #################################################

class Supplier(models.Model):
    company_name = models.CharField(max_length = 250, null = True, blank = True)
    contact_person_name = models.CharField(max_length = 250, null = True, blank = True)
    email = models.EmailField(max_length=254, verbose_name='email address', null = True, blank = True)
    phone = models.CharField(max_length = 25, null = True, blank = True)
    address = models.CharField(max_length = 250, null = True, blank = True)
    city = models.CharField(max_length = 250, null = True, blank = True)
    state = models.CharField(max_length = 250, null = True, blank = True)
    country = models.CharField(max_length = 250, null = True, blank = True)
    postal_code = models.CharField(max_length = 250, null = True, blank = True)
    type_of_goods = models.CharField(max_length = 250)

    def __str__(self):
        return f'{self.company_name} - {self.city} - {self.type_of_goods}'
    