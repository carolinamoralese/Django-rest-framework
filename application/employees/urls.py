from django.urls import path
from . import views

urlpatterns = [
    path("list-employees/", views.EmployeeListView.as_view(), name="employee_list"),
    path(
        "list-employees-by-department/<str:short_name>/",
        views.EmployeeListViewbyDepartment.as_view(),
        name="employee_list_by_department",
    ),
    path(
        "list-employees-by-job/<str:job>/",
        views.EmployeeListViewbyJob.as_view(),
        name="employee_list_by_job",
    ),
    path(
        "list-employees-by-keyword/",
        views.EmployeeListViewbyKeyword.as_view(),
        name="employee_list_by_keyword",
    ),
    path(
        "list-employees-by-hability/",
        views.EmployeeListViewbyHability.as_view(),
        name="employee_list_by_hability",
    ),
    path(
        "see-employee/<pk>/",
        views.EmployeeDetailView.as_view(),
        name="employee_detail",
    ),
    path(
        "add-employee/",
        views.EmployeeCreateView.as_view(),
        name="employee_add",
    ),
]
