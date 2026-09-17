from django.contrib import admin
from .models import Employee, Hability

# Register your models here.
admin.site.register(Hability)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "job", "department", "full_name")
    search_fields = ("name", "last_name", "email", "phone")
    list_filter = ("job", "department")
    filter_horizontal = ("habilities",)

    def full_name(self, obj):
        return f"{obj.name} {obj.last_name}"


admin.site.register(Employee, EmployeeAdmin)
