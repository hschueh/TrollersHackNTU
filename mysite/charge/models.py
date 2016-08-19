from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    level = models.DecimalField(max_digits=3,decimal_places=0)
    exp = models.DecimalField(max_digits=10,decimal_places=0)
    max_exp = models.DecimalField(max_digits=10,decimal_places=0)
    money = models.DecimalField(max_digits=12,decimal_places=0)

class Category(models.Model):
    name = models.CharField(max_length = 100)

class Record(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    spend = models.DecimalField(max_digits=10,decimal_places=0)
    currency = models.CharField(max_length = 10)
    createTime = models.DateTimeField(auto_now_add=True, blank=True)

class Item(models.Model):
    name = models.CharField(max_length = 100)
    value = models.DecimalField(max_digits=5,decimal_places=0)

class User_Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    item = models.ForeignKey(Item,on_delete=models.CASCADE,)



