# coding=utf-8
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext, gettext
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.contrib.auth import login, logout, authenticate
from sistema.forms.professor import *


class ProfessorCreateView(SuccessMessageMixin, CreateView):
    """
    Cadastra um Professor.

    :URL: http://<ip_servidor>/cadastrar-professor/
    """
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor_form.html'
    success_message = gettext('Você foi cadastrado com sucesso')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST['password'])
        self.object.is_active = True
        self.object.save()
        professor = Professor.objects.get(pk=self.object.id)
        user = authenticate(username=professor.username, password=self.request.POST['password'])
        login(self.request, user)
        return super(ProfessorCreateView, self).form_valid(form)


class ProfessorUpdateView(SuccessMessageMixin, UpdateView):
    """
    Atualiza os dados do Professor logado.

    :URL: http://<ip_servidor>/editar-professor/
    """
    model = Professor
    form_class = ProfessorEditForm
    template_name = 'professor_form.html'
    success_message = gettext('Seu perfil foi atualizado com sucesso')

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


class ProfessorDeleteView(SuccessMessageMixin, DeleteView):
    """
    Desativa o Professor logado.

    :URL: http://<ip_servidor>/excluir-professor/
    """
    queryset = Professor.objects.filter()
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        obj = Professor.objects.get(pk=self.request.user.id)
        return obj

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        logout(self.request)
        return super(ProfessorDeleteView, self).form_valid(form)



