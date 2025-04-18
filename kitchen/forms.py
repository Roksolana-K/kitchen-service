from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Dish, Cook, DishType


class DishCreateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(), widget=forms.SelectMultiple()
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Search by name or dish type..."}),
    )


class DishTypeCreateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."}),
    )


class CookCreateForm(UserCreationForm):

    class Meta:
        model = Cook
        fields = [
            "username",
            "email",
            "years_of_experience",
            "is_superuser",
            "is_staff",
        ]


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name", "email", "years_of_experience"]
