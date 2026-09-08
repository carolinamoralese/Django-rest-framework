from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField("Nombre", max_length=50, blank=True)
    short_name = models.CharField("Nombre Corto", max_length=20)
    anulate = models.BooleanField("Anulado", default=False)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ["name"]
        unique_together = ("name", "short_name")

    def __str__(self):
        return f"{self.name} ({self.short_name})"
