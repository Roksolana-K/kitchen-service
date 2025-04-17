from http.client import responses
from itertools import count

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


class LoginTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="123"
        )

    def login_with_correct_credentials(self):
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "123"}, follow=True
        )
        self.assertTrue(response.context["user"].is_authenticated)
        self.assertContains(response, "Logout")

    def login_with_incorrect_credentials(self):
        response = self.client.post(
            reverse("login"), {"username": "anonymous", "password": "123"}
        )
        self.assertFalse(response.context["user"].is_authenticated)
        self.assertContains(
            response,
            "Please enter a correct username and password. Note that both fields may be case-sensitive.",
        )

    def is_redirected_to_home_after_login(self):
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "123"}, follow=True
        )
        self.assertRedirects(response, reverse("home"))


class PermissionTest(TestCase):
    def SetUp(self):
        self.user = get_user_model().objects.create_user(
            username="testUser", password="test123"
        )
        self.superuser = get_user_model().objects.create_superuser(
            username="superuser", password="super123"
        )

    def only_superuser_sees_update_and_create_dishtype(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("kitchen:dish-types-list"))
        self.assertContains(response, "Add new")
        self.assertContains(response, "Update")

    def regular_user_cant_update_and_create_dishtype(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:dish-types-list"))
        self.assertNotContains(response, "Add new")
        self.assertNotContains(response, "Update")

    def only_superuser_can_see_all_details_and_create_new_cook(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("kitchen:cooks-list"))
        cooks_amount = response.context["cooks_amount"]
        self.assertContains(response, "Add new cook")
        self.assertContains(response, "Details", cooks_amount)

    def regular_user_sees_only_his_details_button(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:cooks-list"))
        self.assertContains(response, "Add new cook", count=0)
        self.assertContains(response, "Details", count=1)

    def only_superuser_can_update_and_delete_cook(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("kitchen:cook-details"))
        self.assertContains(response, "Update")
        self.assertContains(response, "Delete")

    def only_superuser_can_mark_superstatus(self):
        self.client.force_login(self.superuser)
        response = self.client.get(reverse("kitchen:cook-create"))
        self.assertContains(response, "Staff status")
        self.assertContains(response, "Superuser status")

    def regular_user_cant_mark_superstatus(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("kitchen:cook-update"))
        self.assertNotContains(response, "Staff status")
        self.assertNotContains(response, "Superuser status")


class SearchFormsTest(TestCase):

    def search_dish_by_name(self):
        user = get_user_model().objects.create_user(
            username="testUser", password="123test"
        )
        dish_type_1 = DishType.objects.create(name="Macaroons")
        dish_type_2 = DishType.objects.create(name="Drinks")

        Dish.objects.create(
            name="Caramel Macaron",
            description="Test",
            dish_type=dish_type_1,
            cooks=user,
        )
        Dish.objects.create(
            name="Pina-colada", description="Test", dish_type=dish_type_2, cooks=user
        )
        response = self.client.get(reverse("kitchen:dishes-list"), {"name": "ca"})
        self.assertEqual(response.status_code, 200)
        dish_name = [d.name for d in response.context["dishes_list"]]
        self.assertIn("Caramel Macaron", dish_name)
        self.assertNotIn("Pina-colada", dish_name)

        self.assertIn("search_form", response.context)
        self.assertEqual(response.context["search_form"].initial["name"], "ca")

    def search_dish_by_dishtype(self):
        user = get_user_model().objects.create_user(
            username="testUser", password="123test"
        )
        dish_type_1 = DishType.objects.create(name="Macaroons")
        dish_type_2 = DishType.objects.create(name="Drinks")

        Dish.objects.create(
            name="Caramel Macaron",
            description="Test",
            dish_type=dish_type_1,
            cooks=user,
        )
        Dish.objects.create(
            name="Pina-colada", description="Test", dish_type=dish_type_2, cooks=user
        )
        response = self.client.get(reverse("kitchen:dishes-list"), {"name": "d"})
        self.assertEqual(response.status_code, 200)
        dish_name = [d.name for d in response.context["dishes_list"]]
        self.assertNotIn("Caramel Macaron", dish_name)
        self.assertIn("Pina-colada", dish_name)

        self.assertIn("search_form", response.context)
        self.assertEqual(response.context["search_form"].initial["name"], "d")


class DishCreationFormTest(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="cook1", password="pass"
        )
        self.user2 = get_user_model().objects.create_user(
            username="cook2", password="pass"
        )

    def cooks_displayed_in_dish_creation_form(self):
        response = self.client.get(reverse("kitchen:dish-create"))
        self.assertContains(response, "cook1")
        self.assertContains(response, "cook2")
