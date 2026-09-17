from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Employee, Hability


class EmployeeListView(ListView):
    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"
    paginate_by = 2


class EmployeeListViewbyDepartment(ListView):
    template_name = "employees/list_by_department.html"
    context_object_name = "employees"

    def get_queryset(self):

        area = self.kwargs["short_name"]

        list_employees = Employee.objects.filter(department__short_name=area)
        return list_employees


class EmployeeListViewbyJob(ListView):
    template_name = "employees/list_by_job.html"
    context_object_name = "employees"

    def get_queryset(self):

        job = self.kwargs["job"]

        mapa = {
            "CONTADOR": "0",
            "ADMINISTRADOR": "1",
            "ECONOMISTA": "2",
            "OTRO": "4",
        }

        clave = mapa.get(job.upper())

        list_employees = Employee.objects.filter(job=clave)
        return list_employees


class EmployeeListViewbyKeyword(ListView):
    template_name = "employees/list_by_keyword.html"
    context_object_name = "employees"

    def get_queryset(self):

        keyword = self.request.GET.get("keyword", "")

        list_employees = Employee.objects.filter(
            name__icontains=keyword
        ) | Employee.objects.filter(last_name__icontains=keyword)
        return list_employees


class EmployeeListViewbyHability(ListView):
    template_name = "employees/list_by_hability.html"
    context_object_name = "habilities"

    def get_queryset(self):

        id_employee = self.request.GET.get("id_employee")

        if not id_employee:
            return Hability.objects.none()

        employee = Employee.objects.get(id=id_employee)

        list_habilities = employee.habilities.all()
        return list_habilities


# EJERCICIO 1


# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     active = models.BooleanField(default=True)

# /employees/?keyword=carolina


# class EmployeeListViewByKeyword(ListView):
#     template_name = "employees/list_by_keyword.html"
#     context_object_name = "employees"

#     def get_queryset(self):
#         keyword = self.request.GET.get("keyword", "")
#         list_employees = Employee.objects.filter(name__icontains=keyword)
#         return list_employees


# EJERCICIO 2

# path(
#     "employees/department/<str:short_name>/",
#     EmployeeListViewByDepartment.as_view()
# )

# /employees/department/contabilidad/

# class EmployeeListViewByDepartment(ListView):
#     template_name = 'employees/list_by_department.html'
#     context_object_name = 'employees'

#     def get_queryset(self):
#         short_name = self.kwargs['short_name']
#         list_employees = Employee.objects.filter(department__short_name=short_name)
#         return list_employees


# EJERCICIO 3


# class EmployeeListViewByHability(ListView):
#     template_name = "employees/listByHability.html"
#     context_object_name = "habilities"

#     def get_queryset(self):
#         id_employee = self.request.GET.get("id_employee")

#         if not id_employee:
#             return Hability.objects.none()

#         employee = Employee.objects.get(id=id_employee)

#         list_habilities = employee.habilities.all()
#         return list_habilities


# Ejercicio 4

# class EmployeeListViewByHability(ListView):
#     template_name = "employees/list_by_employes_with_hability.html"
#     context_object_name = "employees_with_hability"

#     def get_queryset(self):
#         hability = self.request.GET.get("keyword")

#         if not hability:
#             return Employee.objects.none()

#         employee = Employee.objects.filter(habilities__name__icontains=hability)
#         return employee


# Ejercicio 5
# class EmployeeSearchView(ListView):
#     template_name = "employees/search.html"
#     context_object_name = "employees"

#     def get_queryset(self):
#         name = self.request.GET.get("name")
#         hability = self.request.GET.get("hability")

#         if not name and not hability:
#             return Employee.objects.none()

#         filters = {}

#         if name:
#             filters["name__icontains"] = name

#         if hability:
#             filters["habilities__name__icontains"] = hability

#         employees = Employee.objects.filter(**filters)

#         return employees


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "empleado del mes"
        return context
