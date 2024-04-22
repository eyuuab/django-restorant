from django.db import models

# Create menu model

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)