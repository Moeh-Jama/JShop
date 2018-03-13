from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=10, decimal_places=2 )
    #image will be stored at some address and called when displayed.
    image = models.CharField(max_length = 200)

    def __str__(self):
        return self.name