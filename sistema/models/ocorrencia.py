# -*- coding: utf-8 -*-
"""Model de Ocorrência"""
from django.db import models
from django.urls import reverse
from sistema.models.aluno import Aluno
from sistema.models.professor import Professor


class Ocorrencia(models.Model):
    """
    :param professor: models.ForeignKey(Professor, blank=True, null=True)
    :param aluno: models.ForeignKey(Aluno)
    :param disciplina: models.CharField(max_length=250)
    :param descricao: models.TextField(max_length=1000, verbose_name="Descrição da ocorrência")
    :param hora: models.TimeField()
    :param data: models.DateField()
    :param excluido: models.BooleanField(verbose_name="Excluído", default=False)
    """
    professor = models.ForeignKey(Professor, blank=True, null=True)
    aluno = models.ForeignKey(Aluno)
    disciplina = models.CharField(max_length=250)
    descricao = models.TextField(max_length=1000, verbose_name="Descrição da ocorrência")
    hora = models.TimeField()
    data = models.DateField()
    excluido = models.BooleanField(verbose_name="Excluído", default=False)

    def __unicode__(self):
        return '%s' % self.descricao

    def get_absolute_url(self):
        """Método para obter a url absoluta"""
        return reverse('ocorrencia-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = 'sistema'
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'
