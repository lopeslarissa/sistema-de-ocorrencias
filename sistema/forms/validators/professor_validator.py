# coding=utf-8
"""Validador de Username"""
from django.forms import forms
from sistema.models.professor import Professor


def username_validator(nome):
    """Validador de Username de Professor"""
    if Professor.objects.filter(username=nome).exists():
        professor = Professor.objects.get(username=nome)
    else:
        raise forms.ValidationError('Usuário não existe')
    return professor.username
