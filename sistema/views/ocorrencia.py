# coding=utf-8
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext, gettext_lazy
from sistema.models.professor import Professor
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from sistema.forms.ocorrencia import *
from django.contrib.auth.mixins import LoginRequiredMixin


class OcorrenciaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Cadastra uma Ocorrência.

    :URL: http://<ip_servidor>/cadastrar-ocorrencia/
    """
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'
    success_message = gettext_lazy('Ocorrência cadastrada com sucesso')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaCreateView, self).form_valid(form)


class OcorrenciaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Atualiza os dados da Ocorrência selecionada.

    :URL: http://<ip_servidor>/editar-ocorrencia/<id>/
    """
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'
    success_message = gettext_lazy('Ocorrência atualizada com sucesso')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaUpdateView, self).form_valid(form)


class OcorrenciaDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Desativa a Ocorrência selecionada.

    :URL: http://<ip_servidor>/excluir-ocorrencia/<id>/
    """
    queryset = Ocorrencia.objects.filter(excluido=False)
    success_url = reverse_lazy('ocorrencia-list')
    success_message = gettext_lazy('Ocorrência deletada com sucesso')
    login_url = reverse_lazy('login')
    template_name = 'ocorrencia_confirm_delete.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = True
        self.object.save()
        return super(OcorrenciaDeleteView, self).form_valid(form)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OcorrenciaDeleteView, self).delete(request, *args, **kwargs)


class OcorrenciaListView(LoginRequiredMixin, ListView):
    """
    Lista todas as Ocorrências, exceto as desativadas.

    :URL: http://<ip_servidor>/listar-ocorrencias/
    """
    queryset = Ocorrencia.objects.filter(excluido=False)
    template_name = 'ocorrencia_list.html'
    login_url = reverse_lazy('login')


class OcorrenciaDetailView(LoginRequiredMixin, DetailView):
    """
    Exibe os dados da Ocorrência selecionada.

    :URL: http://<ip_servidor>/vizualizar-ocorrencia/<id>/
    """

    queryset = Ocorrencia.objects.filter(excluido=False)
    template_name = 'ocorrencia_detail.html'
    login_url = reverse_lazy('login')



