from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


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
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        )
