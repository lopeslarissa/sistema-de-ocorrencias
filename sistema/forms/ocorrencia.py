# coding=utf-8
from django import forms
from sistema.models.aluno import Aluno
from sistema.models.ocorrencia import Ocorrencia


class OcorrenciaForm(forms.ModelForm):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all().exclude(excluido=True))
    disciplina = forms.CharField(max_length=250, label="Disciplina")
    descricao = forms.CharField(max_length=1000, label="Descrição da ocorrência")
    hora = forms.TimeField(label='Hora')
    data = forms.DateField(label='Data')

    class Meta:
        model = Ocorrencia
        fields = "__all__"
        exclude = ('professor', 'excluido',)
