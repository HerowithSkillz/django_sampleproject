from django.db import models
from django.utils import timezone

# Create your models here.
class CoffeeVariety(models.Model):
    COFFEE_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('BL', 'BLACK'),
        ('WH', 'WHITE'),
        ('ES', 'ESPRESSO'),
        ('CA', 'CAPPUCCINO'),
        ('LT', 'LATTE'),
        ('FR', 'FRAPPUCCINO'),
        ('IC', 'ICED COFFEE'),
        ('OT', 'OTHER'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'coffeeis/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=COFFEE_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
