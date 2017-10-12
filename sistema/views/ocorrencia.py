# coding=utf-8
from sistema.models.professor import Professor
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from sistema.forms.ocorrencia import *


class OcorrenciaCreateView(CreateView):
    """
    Cadastra uma Ocorrência.

    :URL: http://<ip_servidor>/cadastrar-ocorrencia/
    """
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OcorrenciaCreateView, self).get_context_data(**kwargs)
        context['msg'] = 'Ocorrencia cadastrada com sucesso!'
        return context


class OcorrenciaUpdateView(UpdateView):
    """
    Atualiza os dados da Ocorrência selecionada.

    :URL: http://<ip_servidor>/editar-ocorrencia/<id>/
    """
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OcorrenciaUpdateView, self).get_context_data(**kwargs)
        context['msg'] = 'Ocorrencia atualizada com sucesso!'
        return context


class OcorrenciaDeleteView(DeleteView):
    """
    Desativa a Ocorrência selecionada.

    :URL: http://<ip_servidor>/excluir-ocorrencia/<id>/
    """
    queryset = Ocorrencia.objects.filter(excluido=False)
    success_url = reverse_lazy('ocorrencia-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = True
        self.object.save()
        return super(OcorrenciaDeleteView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OcorrenciaDeleteView, self).get_context_data(**kwargs)
        context['msg'] = 'Ocorrencia deletada com sucesso!'
        return context


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



