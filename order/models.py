from pyexpat import model
from django.db import models

# Create your models here.
class Shop(models.Model):
  shops_name = models.CharField(max_length=20)
  shops_address = models.CharField(max_length=40)

class Menu(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  food_name = models.CharField(max_length=20)

class Order(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  order_date = models.DateTimeField('date ordered')
  address = models.CharField(max_length=40)
  estimated_time = models.IntegerField(default=-1)
  deliver_finish = models.BooleanField(default=0)

class OrderFood(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  food_name = models.CharField(max_length=20)
