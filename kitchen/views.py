from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView

from kitchen.forms import (
    DishCreateForm,
    DishSearchForm,
    CookCreateForm,
    CookUpdateForm,
    DishTypeCreateForm,
    DishTypeSearchForm,
)
from kitchen.models import DishType, Dish, Cook


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "kitchen/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_dish_types"] = DishType.objects.count()
        context["dish_count"] = Dish.objects.count()
        context["cooks_count"] = Cook.objects.filter().count()

        return context


class DishListView(LoginRequiredMixin, generic.ListView):
    queryset = Dish.objects.all().order_by("name")
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Dish.objects.select_related("dish_type")
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            search_term = form.cleaned_data["search"]
            if search_term:
                queryset = queryset.filter(
                    Q(name__icontains=search_term)
                    | Q(dish_type__name__icontains=search_term)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = DishSearchForm(self.request.GET)
        return context


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")
    form_class = DishCreateForm


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishCreateForm

    def get_success_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.object.pk})


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_types"
    template_name = "kitchen/dishtype_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types-list")
    form_class = DishTypeCreateForm
    template_name = "kitchen/dishtype_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeCreateForm
    success_url = reverse_lazy("kitchen:dish-types-list")
    context_object_name = "dish_type"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types-list")
    context_object_name = "dish_type"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = "cooks"
    template_name = "kitchen/cooks_list.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    success_url = reverse_lazy("kitchen:cooks-list")
    template_name = "kitchen/cook_form.html"
    form_class = CookCreateForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = CookUpdateForm

    def get_success_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.object.pk})


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("kitchen:cooks-list")
