from django.db import models

from application.departament.models import Department


# Create your models here.
class Employee(models.Model):

    JOB_CHOICES = (
        ("0", "CONTADOR"),
        ("1", "ADMINISTRADOR"),
        ("2", "ECONOMISTA"),
        ("4", "OTRO"),
    )
    name = models.CharField("Nombre", max_length=50, blank=True)
    last_name = models.CharField("Apellido", max_length=50, blank=True)
    email = models.EmailField("Correo Electrónico", max_length=100, blank=True)
    phone = models.CharField("Teléfono", max_length=20, blank=True)
    job = models.CharField("Cargo", max_length=1, choices=JOB_CHOICES, default="4")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Departamento",
    )
    # image = models.ImageField(
    #     "Imagen", upload_to="employees/", default="employees/default.png"
    # )

    def __str__(self):
        return f"{self.name} {self.last_name}"
