# coding=utf-8
from sistema.models.aluno import Aluno
from django import forms


class AlunoForm(forms.ModelForm):
    nome = forms.CharField(max_length=250, label="Nome")
    email = forms.EmailField(label="E-mail")
    telefone = forms.CharField(max_length=11, label='Telefone')
    turma = forms.CharField(max_length=250, label='Turma')
    curso = forms.CharField(max_length=250, label="Curso")
    matricula = forms.CharField(max_length=250, label="Matrícula")

    class Meta:
        model = Aluno
        fields = "__all__"
        exclude = ('excluido',)

