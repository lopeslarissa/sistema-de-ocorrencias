# coding=utf-8
from sistema.forms.validators.professor_validator import *
from sistema.models.professor import Professor
from django import forms


class ProfessorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Professor
        fields = ('first_name', 'last_name', 'email', 'password', 'username',)

    def clean_username(self):
        username=self.cleaned_data['username']
        if Professor.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuário já existe')
        return username


class ProfessorEditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Professor
        fields = ('first_name', 'last_name', 'email', 'password',)
