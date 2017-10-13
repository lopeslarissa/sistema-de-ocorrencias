# coding=utf-8
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext
from sistema.models.professor import Professor
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from sistema.forms.ocorrencia import *


class OcorrenciaCreateView(SuccessMessageMixin, CreateView):
    """
    Cadastra uma Ocorrência.

    :URL: http://<ip_servidor>/cadastrar-ocorrencia/
    """
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'
    success_message = ugettext('Ocorrência cadastrada com sucesso')

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaCreateView, self).form_valid(form)


class OcorrenciaUpdateView(SuccessMessageMixin, UpdateView):
    """
    Atualiza os dados da Ocorrência selecionada.

    :URL: http://<ip_servidor>/editar-ocorrencia/<id>/
    """
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'
    success_message = ugettext('Ocorrência atualizada com sucesso')

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaUpdateView, self).form_valid(form)


class OcorrenciaDeleteView(SuccessMessageMixin, DeleteView):
    """
    Desativa a Ocorrência selecionada.

    :URL: http://<ip_servidor>/excluir-ocorrencia/<id>/
    """
    queryset = Ocorrencia.objects.filter(excluido=False)
    success_url = reverse_lazy('ocorrencia-list')
    success_message = ugettext('Ocorrência deletada com sucesso')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = True
        self.object.save()
        return super(OcorrenciaDeleteView, self).form_valid(form)


class OcorrenciaListView(ListView):
    """
    Lista todas as Ocorrências, exceto as desativadas.

    :URL: http://<ip_servidor>/listar-ocorrencias/
    """
    queryset = Ocorrencia.objects.filter(excluido=False)
    template_name = 'ocorrencia_list.html'


class OcorrenciaDetailView(DetailView):
    """
    Exibe os dados da Ocorrência selecionada.

    :URL: http://<ip_servidor>/vizualizar-ocorrencia/<id>/
    """

    queryset = Ocorrencia.objects.filter(excluido=False)
    template_name = 'ocorrencia_detail.html'



