from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    level = models.DecimalField(max_digits=3,decimal_places=0,default=1)
    exp = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    max_exp = models.DecimalField(max_digits=10,decimal_places=0,default=100)
    money = models.DecimalField(max_digits=12,decimal_places=0,default=0)
    dps = models.DecimalField(max_digits=5,decimal_places=0,default=1)
    facebookID = models.CharField(max_length = 100,default="")
    token = models.CharField(max_length = 200,default="")
    gender = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length = 100)
    income = models.BooleanField(default=False)

class Record(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    spend = models.DecimalField(max_digits=10,decimal_places=0)
    currency = models.CharField(max_length = 10)
    createTime = models.DateTimeField(auto_now_add=True, blank=True)

class Item(models.Model):
    name = models.CharField(max_length = 100)
    itemType = models.CharField(max_length = 10,default="equipment")
    attack = models.DecimalField(max_digits=5,decimal_places=0)
    duration = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    expiredTime = models.DateTimeField(blank=True,default="0")
    cost = models.DecimalField(max_digits=5,decimal_places=0,default=0)
    pngFile = models.CharField(max_length = 200,default="")

class User_Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    item = models.ForeignKey(Item,on_delete=models.CASCADE,)

class UserExp(models.Model):
    level = models.DecimalField(max_digits=4,decimal_places=0)
    required_exp = models.DecimalField(max_digits=12,decimal_places=0)

class Monster(models.Model):
    name = models.CharField(max_length = 100,default="Boss")
    level = models.DecimalField(max_digits=4,decimal_places=0)
    hp = models.DecimalField(max_digits=20,decimal_places=0)
    exp = models.DecimalField(max_digits=9,decimal_places=0)
    money = models.DecimalField(max_digits=9,decimal_places=0)
    pngFile = models.CharField(max_length = 200)

class User_Monster(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    monster = models.ForeignKey(Monster,on_delete=models.CASCADE,)
    current_hp = models.DecimalField(max_digits=20,decimal_places=0)
    createTime = models.DateTimeField(auto_now_add=True, blank=True)

class Missions(models.Model):
    name = models.CharField(max_length = 100,default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    missionType = models.CharField(max_length = 40)
    status = models.CharField(max_length = 20)
    createTime = models.DateTimeField(auto_now_add=True, blank=True)

class ConsecutiveLoginMission(models.Model):
    mission = models.ForeignKey(Missions,on_delete=models.CASCADE,default=None)
    days = models.DecimalField(max_digits=4,decimal_places=0)
    required_days = models.DecimalField(max_digits=4,decimal_places=0)
    exp = models.DecimalField(max_digits=10,decimal_places=0)
    money = models.DecimalField(max_digits=10,decimal_places=0)

class ConsecutiveConsumeMission(models.Model):
    mission = models.ForeignKey(Missions,on_delete=models.CASCADE,default=None)
    expiredTime = models.DateTimeField(blank=True,default = None)
    targetCategory = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    exp = models.DecimalField(max_digits=10,decimal_places=0)
    money = models.DecimalField(max_digits=10,decimal_places=0)
    currentConsume = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    requiredConsume = models.DecimalField(max_digits=10,decimal_places=0,default=0)


class ConsecutiveBudgetMission(models.Model):
    mission = models.ForeignKey(Missions,on_delete=models.CASCADE,default=None)
    days = models.DecimalField(max_digits=4,decimal_places=0)
    required_days = models.DecimalField(max_digits=4,decimal_places=0)
    budget = models.DecimalField(max_digits=8,decimal_places=0)
    exp = models.DecimalField(max_digits=10,decimal_places=0)
    money = models.DecimalField(max_digits=10,decimal_places=0)

class MealMission(models.Model):
    mission = models.ForeignKey(Missions,on_delete=models.CASCADE,default=None)
    meal = models.CharField(max_length = 20)
    expiredTime = models.DateTimeField(blank=True,default=None)
    exp = models.DecimalField(max_digits=10,decimal_places=0)
    money = models.DecimalField(max_digits=10,decimal_places=0)

class RandomMission(models.Model):
    mission = models.ForeignKey(Missions,on_delete=models.CASCADE,)
    targetItem = models.ForeignKey(Item,on_delete=models.CASCADE,default=None)
    amount = models.DecimalField(max_digits=10,decimal_places=0)
    expiredTime = models.DateTimeField(blank=True)
    exp = models.DecimalField(max_digits=10,decimal_places=0)
    money = models.DecimalField(max_digits=10,decimal_places=0)









