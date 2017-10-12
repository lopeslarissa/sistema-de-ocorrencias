# coding: utf-8
from django.db import models
from django.urls import reverse


class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=11)
    turma = models.CharField(max_length=250)
    curso = models.CharField(max_length=250)
    matricula = models.CharField(max_length=250)
    excluido = models.BooleanField(verbose_name='Excluído', default=False)

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('aluno-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = 'sistema'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
