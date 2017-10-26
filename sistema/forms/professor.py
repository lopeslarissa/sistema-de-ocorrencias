# coding=utf-8
"""Formulários de Professor"""
from sistema.models.professor import Professor
from django import forms


class ProfessorForm(forms.ModelForm):
    """Formulário de cadastro de professor"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Professor
        fields = ('first_name', 'last_name', 'email', 'password', 'username',)

    def clean_username(self):
        """Método que verifica se o username já existe"""
        username = self.cleaned_data['username']
        if Professor.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuário já existe')
        return username


class ProfessorEditForm(forms.ModelForm):
    """Formulário de edição de professor"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Professor
        fields = ('first_name', 'last_name', 'email', 'password',)
