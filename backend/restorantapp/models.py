from django.db import models

# Create menu model

class UserModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    balance = models.IntegerField(default=1000)

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

