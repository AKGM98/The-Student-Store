from django.contrib import admin

# Register your models here.
from.models import Product
admin.site.register(Product)
from.models import Product_uniform
admin.site.register(Product_uniform)
from.models import Product_laptop
admin.site.register(Product_laptop)
from.models import Product_tablet
admin.site.register(Product_tablet)
from.models import Product_stationery
admin.site.register(Product_stationery)
from.models import  Cart
admin.site.register(Cart)
from.models import  Pdf
admin.site.register(Pdf)