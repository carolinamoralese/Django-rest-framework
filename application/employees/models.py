from django.db import models

from application.departament.models import Department

from ckeditor.fields import RichTextField


class Hability(models.Model):
    hability = models.CharField("Habilidad", max_length=50, blank=True)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ["hability"]
        unique_together = ("hability",)

    def __str__(self):
        return f"{self.hability}"


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
    habilities = models.ManyToManyField(
        Hability, related_name="employees_with_ability", verbose_name="Habilidades"
    )
    cvdocument = RichTextField("Hoja de Vida", blank=True, null=True)
    # image = models.ImageField(
    #     "Imagen", upload_to="employees/", default="employees/default.png"
    # )

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["job", "name", "last_name"]
        unique_together = ("email", "phone")

    def __str__(self):
        return f"{self.name} {self.last_name}"
