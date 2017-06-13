# coding=utf-8
from sistema.forms.validators.professor_validator import *
from sistema.models.professor import Professor
from django import forms
from django.contrib.auth import authenticate


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


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Professor
        fields = ('password', 'username',)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if Professor.objects.filter(username = username).exists():
            username = Professor.objects.get(username=username)
            if authenticate(username=username, password=password) is None:
                raise forms.ValidationError("Usuário ou senha incorretos")
        return self.cleaned_data

    def clean_username(self):
        return UsernameValidator(self.cleaned_data['username'])
