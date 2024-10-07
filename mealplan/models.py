"""Models for meal plans."""
from django.contrib.auth.models import User, AnonymousUser
from django.db import models
from django.template.defaultfilters import slugify
from time import time

class Mealplan(models.Model):
    name = models.CharField(max_length=100, default="")
    monday = models.CharField(max_length=100, default="")
    tuesday = models.CharField(max_length=100, default="")
    wednesday = models.CharField(max_length=100, default="")
    thursday = models.CharField(max_length=100, default="")
    friday = models.CharField(max_length=100, default="")
    saturday = models.CharField(max_length=100, default="")
    sunday = models.CharField(max_length=100, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    slug = models.SlugField(default="")

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(f"{self.name} {time()}")
        super(Mealplan, self).save(*args, **kwargs)
