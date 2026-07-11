from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Person

# Create your views here.


class HomeView(TemplateView):
    template_name = "home/home.html"


class HomeListView(ListView):
    template_name = "home/list.html"
    queryset = [
        {"name": "John Doe", "age": 30},
        {"name": "Jane Smith", "age": 25},
        {"name": "Alice Johnson", "age": 28},
    ]
    context_object_name = "people"


class ModelListView(ListView):
    model = Person
    template_name = "home/model_list.html"
    context_object_name = "persons"
