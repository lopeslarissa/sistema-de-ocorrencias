# coding=utf-8
from django import forms
from django.utils.translation import gettext_lazy

from sistema.models.aluno import Aluno
from sistema.models.ocorrencia import Ocorrencia


class OcorrenciaForm(forms.ModelForm):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all().exclude(excluido=True), label=gettext_lazy("Aluno"))
    disciplina = forms.CharField(max_length=250, label=gettext_lazy("Disciplina"))
    descricao = forms.CharField(max_length=1000, label=gettext_lazy("Descrição da ocorrência"))
    hora = forms.TimeField(label=gettext_lazy('Hora'))
    data = forms.DateField(label=gettext_lazy('Data'))

    class Meta:
        model = Ocorrencia
        fields = "__all__"
        exclude = ('professor', 'excluido',)
