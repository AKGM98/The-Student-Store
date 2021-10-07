from django.db import models

# Create your models here.
class Product(models.Model):
    product_image = models.ImageField(upload_to="ssproject/images", default="")
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class Product_uniform(models.Model):
    productu_image = models.ImageField(upload_to="ssproject/images", default="")
    productu_name = models.CharField(max_length=20)
    productu_price = models.IntegerField()
    productu_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.productu_name

class Product_laptop(models.Model):
    productl_image = models.ImageField(upload_to="ssproject/images", default="")
    productl_name = models.CharField(max_length=20)
    productl_price = models.IntegerField()
    productl_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.productl_name

class Product_tablet(models.Model):
    producttab_image = models.ImageField(upload_to="ssproject/images", default="")
    producttab_name = models.CharField(max_length=20)
    producttab_price = models.IntegerField()
    producttab_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.producttab_name

class Product_stationery(models.Model):
    productst_image = models.ImageField(upload_to="ssproject/images", default="")
    productst_name = models.CharField(max_length=20)
    productst_price = models.IntegerField()
    productst_desc = models.CharField(max_length=100)

    def __str__(self):
     return self.productst_name

class Cart(models.Model):
    productu_name = models.ManyToManyField(Product_uniform, null=True)
    cart_price = models.IntegerField(max_length=50, null="true")


class Pdf(models.Model):
    pdf_name = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to="ssproject/pdf", default="")





