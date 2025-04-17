from django.urls import path, include

from kitchen.views import (
    HomePageView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    CookListView,
    CookDetailView,
    CookUpdateView,
    CookCreateView,
    CookDeleteView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]

app_name = "kitchen"
