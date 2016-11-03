from django.db import models
from ioteca_service_apps.eventos.choices.montos import PAGO_INASISTENCIA_CHOICES


class TimeStampModel(models.Model):

    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "TimeStampModel"
        verbose_name_plural = "TimeStampModels"


class Inasistencia(TimeStampModel):

    monto = models.CharField(max_length=2, choices=PAGO_INASISTENCIA_CHOICES)
    num_inasistencias = models.IntegerField()

    class Meta:
        verbose_name = "Inasistencia"
        verbose_name_plural = "Inasistencias"

    def __str__(self):
        return self.nombre
