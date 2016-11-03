from django.db import models
from ioteca_service_apps.asociacion.models.lote import Lote
from .evento import Evento, TimeStampModel


class Asistencia(TimeStampModel):

    evento = models.ForeignKey(Evento)
    lote = models.ForeignKey(Lote)
    dni_representante = models.CharField(max_length=8, null=True, blank=True)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return self.dni_representante
