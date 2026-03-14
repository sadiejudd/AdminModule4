from django.db import models


# Create your models here.





class Category(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length= 50, null= False)

    def __str__(self):
        return self.name

 

 

class Product(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField( max_length = 200)
    price = models.DecimalField(decimal_places= 2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    tag = models.ManyToManyField(Tag, through = "ProductTag")

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


