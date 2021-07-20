from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField.max_length
    url = models.CharField(max_length=200)

class Category(models.Model):
    group = models.CharField(max_length=20)

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    recipe_ingredient = models.ManyToManyField(Recipe, through='Recipe_Ingredient')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField
    unit = models.CharField(max_length=5)

class Dietary_requirement(models.Model):
    type = models.CharField(max_length=20)
    dietary_category = models.ManyToManyField(Category, through='Dietary_Category')

class Dietary_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dietary_requirement = models.ForeignKey(Dietary_requirement, on_delete=models.CASCADE)
