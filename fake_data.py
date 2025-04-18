import os
from decimal import Decimal
import django
import random

from django.contrib.auth import get_user_model
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitchen_service.settings")
django.setup()

from kitchen.models import Dish, DishType, Cook

from django.core.management.base import BaseCommand


fake = Faker()

def generate_fake_data():
    DishType.objects.all().delete()
    Cook.objects.all().delete()
    Dish.objects.all().delete()

    dishtype_list = []
    dish_type_names = [
        "Starter", "Main Course", "Dessert", "Salad", "Soup",
        "Beverage", "Side Dish", "Appetizer", "Snack", "Breakfast",
        "Brunch", "Grill", "Pasta", "Seafood", "Vegan",
        "Vegetarian", "Meat"
    ]
    for name in dish_type_names:
        dish_type = DishType.objects.create(name=name)
        dishtype_list.append(dish_type)

    cooks_list = []
    for _ in range(20):
        cook = Cook.objects.create(
            username="cook_" + fake.name(),
            password="password",
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            years_of_experience=random.randint(1, 10),
        )
        cooks_list.append(cook)

    dish_names = [
    "Spicy Mango Chicken", "Garlic Butter Shrimp Pasta", "Creamy Tomato Basil Soup", "Thai Green Curry",
    "Honey Glazed Salmon", "Mushroom Risotto", "Crispy Tofu Stir-Fry", "Beef Stroganoff", "Eggplant Parmesan",
    "Korean BBQ Ribs", "Lemon Herb Roasted Chicken", "Butternut Squash Ravioli", "Moroccan Chickpea Stew",
    "Pulled Pork Sliders", "Teriyaki Noodle Bowl", "Classic Caesar Salad", "Sweet Chili Cauliflower",
    "Cheesy Baked Ziti", "BBQ Chicken Flatbread", "Zucchini Fritters"
    ]
    for _ in range(20):
        dish = Dish.objects.create(
            name=random.choice(dish_names),
            description=fake.text(max_nb_chars=150),
            price=Decimal(random.randint(1, 100)),
            dish_type=random.choice(dishtype_list),
        )
        assigned_cooks = random.sample(cooks_list, k=random.randint(1, 3))
        dish.cooks.set(assigned_cooks)
