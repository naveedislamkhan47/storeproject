from django.db import models
from .Suppliers import Supplier
from django.utils.text import slugify
######################################        Models for Product     ############################################

#main collection Like Men or Women
class Collection(models.Model):
    title = models.CharField(max_length = 15, blank = False,  unique = True)
    slug = models.SlugField(max_length=25, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}'s"

###############################################   END   ##############################################

#CATEGORY for the nature of Product e.g Shoes , Apparel , Accessories etc
class Product_Cat(models.Model):
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    title = models.CharField(max_length = 25, blank = False)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    """now we want this model's slug field to be the combination of (Collection Title + Product's Category title ).
    To achieve this we will modify model's save method before calling it ,in following way:
    1 - import join function
    2 - use '-' as separator
    3 - join slug from Collection(foregin Key) with title of current model """
    
    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.collection.slug), slugify(self.title)))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}"

###############################################   END   ##############################################


#CATEGORY for the Nature Of Item e.g Shoes may include formal,regular,sports
class Item_Cat(models.Model):
    product_cat = models.ForeignKey(Product_Cat, on_delete = models.PROTECT)
    title = models.CharField(max_length = 25, blank = False)
    slug = models.SlugField(max_length=75, unique=True, null=True)
    
    #slug is assigned value just like before by combining parrent's category slug with current category's title
    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.product_cat.slug), slugify(self.title)))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}"
###############################################   END   ##############################################
###########################  ABOVE WERE ALL THE CATEGORIES OF A PRODUCT  #############################
######################################################################################################


######################  BELLOW IS THE MAIN PRODUCT MODEL AND ITS DETAILS MODEL  ######################

class Product(models.Model):
    item_cat = models.ForeignKey(Item_Cat, on_delete = models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 255, blank = False)
    description = models.TextField(max_length = 500, blank = True)
    unit_price = models.DecimalField(max_digits = 9, decimal_places = 2, blank = False)
    weight_grams = models.PositiveIntegerField(verbose_name = 'Weight (Grams)')
    quantity = models.PositiveSmallIntegerField(default = 0)
    out_of_stock = models.BooleanField(default = False)
    discount_allowed = models.BooleanField(default = False)
    discount_value = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)
    ranking = models.PositiveSmallIntegerField(default = 10)
    active = models.BooleanField(default = False)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank = False)
    note = models.CharField(max_length = 250, null = True)
    image = models.ImageField(default = 'default.png', upload_to='product-pics')

    #slug is assigned the value just like before by combining parrent's category slug with current products's name
    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.item_cat.slug), slugify(self.name)))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.slug}"

###############################################   END   ##############################################

class Product_Detail(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    color = models.CharField(max_length = 50, null = True, blank = True)
    size = models.CharField(max_length = 50, null = True, blank = True)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    note = models.CharField(max_length = 250 , null = True, blank = True)

    #slug is assigned value just like before by combining product's slug with product's color,size etc
    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.product.slug), slugify(self.color)))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.slug}"

###############################################   END   ##############################################
######################################################################################################