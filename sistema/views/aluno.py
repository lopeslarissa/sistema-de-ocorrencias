# coding=utf-8
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import ugettext, gettext_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from sistema.forms.aluno import AlunoForm
from sistema.models.aluno import Aluno
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class AlunoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Cadastra um Aluno.

    :URL: http://<ip_servidor>/cadastrar-aluno/
    """
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'
    success_message = gettext_lazy('Aluno cadastrado com sucesso')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = False
        self.object.save()
        return super(AlunoCreateView, self).form_valid(form)


class AlunoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Atualiza os dados do Aluno selecionado.

    :URL: http://<ip_servidor>/editar-aluno/<id>/
    """
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'
    success_message = gettext_lazy('Aluno atualizado com sucesso')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = False
        self.object.save()
        return super(AlunoUpdateView, self).form_valid(form)


class AlunoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Desativa o Aluno selecionado.

    :URL: http://<ip_servidor>/excluir-aluno/<id>/
    """
    queryset = Aluno.objects.filter(excluido=False)
    success_url = reverse_lazy('aluno-list')
    success_message = gettext_lazy('Aluno excluído com sucesso')
    login_url = reverse_lazy('login')
    template_name = 'aluno_confirm_delete.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = True
        self.object.save()
        return super(AlunoDeleteView, self).form_valid(form)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AlunoDeleteView, self).delete(request, *args, **kwargs)


class AlunoListView(LoginRequiredMixin, ListView):
    """
    Lista todos os Alunos, exceto os desativados.

    :URL: http://<ip_servidor>/listar-aluno/
    """
    queryset = Aluno.objects.filter(excluido=False)
    template_name = 'aluno_list.html'
    login_url = reverse_lazy('login')


class AlunoDetailView(LoginRequiredMixin, DetailView):
    """
    Exibe os dados do Aluno selecionado.

    :URL: http://<ip_servidor>/vizualizar-aluno/<id>/
    """
    queryset = Aluno.objects.filter(excluido=False)
    template_name = 'aluno_detail.html'
    login_url = reverse_lazy('login')
