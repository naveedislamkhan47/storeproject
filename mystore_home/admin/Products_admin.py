from django.contrib import admin
from mystore_home.models import Collection, Product, Product_Cat, Item_Cat, Product_Detail

#Register Products Models here

class uneditable_slug(admin.ModelAdmin):
    readonly_fields=('slug', )

admin.site.register(Collection, uneditable_slug)
admin.site.register(Product, uneditable_slug)
admin.site.register(Product_Cat, uneditable_slug)
admin.site.register(Item_Cat, uneditable_slug)
admin.site.register(Product_Detail , uneditable_slug)