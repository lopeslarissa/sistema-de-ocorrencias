# coding=utf-8
"""Views de Professor"""
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from sistema.forms.professor import ProfessorForm, ProfessorEditForm
from sistema.models.professor import Professor


class ProfessorCreateView(SuccessMessageMixin, CreateView):
    """
    Cadastra um Professor.

    :URL: http://<ip_servidor>/cadastrar-professor/
    """
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor_form.html'
    success_message = gettext_lazy('Você foi cadastrado com sucesso')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST['password'])
        self.object.is_active = True
        self.object.save()
        professor = Professor.objects.get(pk=self.object.id)
        user = authenticate(username=professor.username, password=self.request.POST['password'])
        login(self.request, user)
        return super(ProfessorCreateView, self).form_valid(form)


class ProfessorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Atualiza os dados do Professor logado.

    :URL: http://<ip_servidor>/editar-professor/
    """
    model = Professor
    form_class = ProfessorEditForm
    template_name = 'professor_form.html'
    success_message = gettext_lazy('Seu perfil foi atualizado com sucesso')
    login_url = reverse_lazy('login')
    success_url = '/editar-professor/'

    def get_object(self, queryset=None):
        obj = User.objects.get(pk=self.request.user.id)
        return obj

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST['password'])
        self.object.is_active = True
        self.object.save()
        professor = Professor.objects.get(pk=self.object.id)
        user = authenticate(username=professor.username, password=self.request.POST['password'])
        login(self.request, user)
        return super(ProfessorUpdateView, self).form_valid(form)


class ProfessorDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Desativa o Professor logado.

    :URL: http://<ip_servidor>/excluir-professor/
    """
    queryset = Professor.objects.filter()
    success_url = reverse_lazy('login')
    login_url = reverse_lazy('login')
    template_name = 'professor_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = Professor.objects.get(pk=self.request.user.id)
        return obj

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        logout(self.request)
        return super(ProfessorDeleteView, self).form_valid(form)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProfessorDeleteView, self).delete(request, *args, **kwargs)
