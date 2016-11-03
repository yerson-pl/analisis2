from django.db import models
from ioteca_service_apps.asociacion.models.socio_lote import SocioLote
from .evento import Evento


class TimeStampModel(models.Model):

    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "TimeStampModel"
        verbose_name_plural = "TimeStampModels"


class Asistencia(TimeStampModel):

    evento = models.ForeignKey(Evento)
    socio = models.ForeignKey(SocioLote)
    dni_representante = models.CharField(max_length=8, null=True, blank=True)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return self.dni_representante
