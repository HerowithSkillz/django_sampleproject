from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

# One to many relationship

class CoffeeReview(models.Model):
    coffee = models.ForeignKey(CoffeeVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.coffee.name}'

# Many to many 
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    coffee_varieties = models.ManyToManyField(CoffeeVariety, related_name='stores')

    def __str__(self):
        return self.name

# One to One relationship
class CoffeeCertification(models.Model):
    coffee = models.OneToOneField(CoffeeVariety, on_delete=models.CASCADE, related_name='certification')
    certification_number = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.coffee.name}'