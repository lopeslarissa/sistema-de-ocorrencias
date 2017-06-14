# coding=utf-8
from django.forms import forms
from sistema.models.professor import Professor


def UsernameValidator(nome):
    if Professor.objects.filter(username=nome).exists():
        professor = Professor.objects.get(username=nome)
    else:
        raise forms.ValidationError('Usuário não existe')
    return professor.username
