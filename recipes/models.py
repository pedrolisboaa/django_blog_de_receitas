from ast import mod
from distutils.command.upload import upload
from statistics import mode
from turtle import update
from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=175)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=70)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=75)
    preparation_steps = models.TextField()
    preparaation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(uploada_to='recipes/cover/%Y/%m/%d/')


