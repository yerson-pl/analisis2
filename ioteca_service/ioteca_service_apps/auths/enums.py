# -*- coding: utf-8 -*-
"""
Enums de la app
"""
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst

WEB = 'WEB'
ADMISION = 'ADMISION'
BACKEND = 'BACKEND'
OTHER = 'OTHER'
MODULE_CHOICES = (
    (WEB, 'Web informativa'),
    (ADMISION, 'Admisión'),
    (BACKEND, 'Backend Manager'),
    (OTHER, capfirst(_('other'))),
)


HIERARCHY_TYPE_CHOICES = (
    ('INSTITUCION', 'Institucion'),
    ('FILIAL', 'Filial'),
    ('FACULTAD', 'Facultad'),
    ('ESCUELA', 'Escuela'),
    ('CARRERA', 'Carrera'),
    ('DEPARTAMENTO_ACAD', 'Departamento acad.'),
    (OTHER, capfirst(_('other'))),
)

M = 'M'
F = 'F'
GENRE_CHOICES = (
    (M, _('Masculino')),
    (F, capfirst(_('Femenino'))),
)

SOLTERO = 'Soltero'
CASADO = 'Casado'
VIUDO = 'Viudo'
DIVORCIADO = 'Divorsiado'
ESTADO_CIVIL_CHOICES = (
    (SOLTERO, 'Soltero'),
    (CASADO, 'Casado'),
    (VIUDO, 'Viudo'),
    (DIVORCIADO, 'Divorsiado')
)

S = 'Si'
N = 'No'
SELECT_SN_CHOICES = (
    (S, 'Si'),
    (N, 'No')
)
