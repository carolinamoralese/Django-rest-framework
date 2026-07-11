from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField("Nombre", max_length=50, blank=True)
    short_name = models.CharField("Nombre Corto", max_length=20)
    anulate = models.BooleanField("Anulado", default=False)

    def __str__(self):
        return f"{self.name} ({self.short_name})"
