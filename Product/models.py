from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length = 200)
    GAMES = 'Game'
    LAPTOP = 'Laptop'
    ELECTRONICS ='Electronic'
    MISC = 'Misc'
    PRODUCT_CATEGORIES = (
        (GAMES, 'Games'),
        (LAPTOP, 'Laptops'),
        (ELECTRONICS ,'Electronics'),
        (MISC, 'Misc')
    )
    category = models.CharField(
        max_length = 200,
        choices = PRODUCT_CATEGORIES,
        default = MISC
    )
   # category = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=10, decimal_places=2 )
    #image will be stored at some address and called when displayed.
    image = models.CharField(max_length = 200)



class Games(models.Model):
    Game_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Age_Restriction = models.IntegerField()
   # Developer = models.CharField(max_length = 200)
    year_of_publish = models.DateField()
    Platform = models.CharField(max_length = 200)
    Quantity = models.IntegerField()        