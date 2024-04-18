
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Foods(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='foods/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.ForeignKey(Foods, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    paid_amount = models.IntegerField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.name
    


















    

    
    
    
    
