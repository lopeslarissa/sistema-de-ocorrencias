# coding=utf-8
"""Formulário de aluno"""
from django import forms
from django.utils.translation import gettext_lazy
from sistema.models.aluno import Aluno


class AlunoForm(forms.ModelForm):
    """Formulário de cadastro de aluno"""
    nome = forms.CharField(max_length=250, label=gettext_lazy("Nome"))
    email = forms.EmailField(label=gettext_lazy("E-mail"))
    telefone = forms.CharField(max_length=11, label=gettext_lazy('Telefone'))
    turma = forms.CharField(max_length=250, label=gettext_lazy('Turma'))
    curso = forms.CharField(max_length=250, label=gettext_lazy("Curso"))
    matricula = forms.CharField(max_length=250, label=gettext_lazy("Matrícula"))

    class Meta:
        model = Aluno
        fields = "__all__"
        exclude = ('excluido',)
