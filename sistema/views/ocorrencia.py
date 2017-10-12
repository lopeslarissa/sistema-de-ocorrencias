# coding=utf-8
from sistema.models.professor import Professor
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from sistema.forms.ocorrencia import *


class OcorrenciaCreateView(CreateView):
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaCreateView, self).form_valid(form)


class OcorrenciaUpdateView(UpdateView):
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencia_form.html'

    def form_valid(self, form):
        professor = Professor.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.professor = professor
        self.object.save()
        return super(OcorrenciaUpdateView, self).form_valid(form)


class OcorrenciaDeleteView(DeleteView):
    queryset = Ocorrencia.objects.filter(excluido=False)
    success_url = reverse_lazy('ocorrencia-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = True
        self.object.save()
        return super(OcorrenciaDeleteView, self).form_valid(form)


class OcorrenciaListView(ListView):
    '''
    Lista todos as Atividades.

    :URL: http://<ip_servidor>/atividade/atividade/list/
    '''
    queryset = Ocorrencia.objects.filter(excluido=False)
    template_name = 'ocorrencia_list.html'


class OcorrenciaDetailView(DetailView):
    '''
    Exibe, *atualiza* e `deleta` uma Atividade específica.

    :URL: http://<ip_servidor>/atividade/atividade/<id>/
    '''

    queryset = Ocorrencia.objects.filter(excluido=False)
    template_name = 'ocorrencia_detail.html'



