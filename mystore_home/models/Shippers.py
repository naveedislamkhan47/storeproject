from django.db import models
############################# Shippinfg COmpanies ####################################
class Shipper(models.Model):
    company_name = models.CharField(max_length = 150)
    branch = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)

    def __str__(self):
        return f'{self.company_name} - {self.branch}'