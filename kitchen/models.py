from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.username} - {self.years_of_experience} - {self.email}"


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    dish_type = models.ForeignKey(
        DishType, related_name="dish_type", on_delete=models.CASCADE
    )
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    def __str__(self):
        return f"{self.name} - {self.description} - {self.dish_type} - {self.cooks}"
