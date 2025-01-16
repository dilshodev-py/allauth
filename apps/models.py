
from django.db import models
from django.db.models import Model, CharField, CASCADE
from django.db.models.fields import DecimalField


# Create your models here.



# class Product(Model):
#     name = CharField(max_length=255)
#     price = DecimalField(max_digits=10 ,decimal_places= 0)


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey("Category", related_name='ingredients' , on_delete=CASCADE)

    def __str__(self):
        return self.name

class Question(Model):
    question = CharField(max_length=255)