# coding=utf-8
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.contrib.auth import login, logout, authenticate
from sistema.forms.professor import *


class ProfessorCreateView(CreateView):
    """
    Cadastra um Professor.

    :URL: http://<ip_servidor>/cadastrar-professor/
    """
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST['password'])
        self.object.is_active = True
        self.object.save()
        professor = Professor.objects.get(pk=self.object.id)
        user = authenticate(username=professor.username, password=self.request.POST['password'])
        login(self.request, user)
        return super(ProfessorCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProfessorCreateView, self).get_context_data(**kwargs)
        context['msg'] = 'Você foi cadastrado com sucesso!'
        return context


class ProfessorUpdateView(UpdateView):
    """
    Atualiza os dados do Professor logado.

    :URL: http://<ip_servidor>/editar-professor/
    """
    model = Professor
    form_class = ProfessorEditForm
    template_name = 'professor_form.html'

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

    def get_context_data(self, **kwargs):
        context = super(ProfessorUpdateView, self).get_context_data(**kwargs)
        context['msg'] = 'Seu perfil foi atualizado com sucesso!'
        return context


class ProfessorDeleteView(DeleteView):
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



