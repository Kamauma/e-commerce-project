from django.db import models
from django.contrib.auth.models import User

# Extend Django's built-in User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


# Product model with categories
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('phones', 'Phones'),
        ('appliances', 'Home Appliances'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='phones')
    image = models.ImageField(upload_to='products/', blank=True, null=True, default= 'products/placeholder.png')

    def __str__(self):
        return self.name
