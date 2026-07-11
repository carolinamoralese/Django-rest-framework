from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("list/", views.HomeListView.as_view(), name="home_list"),
    path("list-model/", views.ModelListView.as_view(), name="home_model_list"),
]
