# coding=utf-8
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from sistema.forms.aluno import *


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = False
        self.object.save()
        return super(AlunoCreateView, self).form_valid(form)


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = False
        self.object.save()
        return super(AlunoUpdateView, self).form_valid(form)


class AlunoDeleteView(DeleteView):
    queryset = Aluno.objects.filter(excluido=False)
    success_url = reverse_lazy('aluno-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = True
        self.object.save()
        return super(AlunoDeleteView, self).form_valid(form)


class AlunoListView(ListView):
    '''
    Lista todos as Atividades.

    :URL: http://<ip_servidor>/atividade/atividade/list/
    '''
    queryset = Aluno.objects.filter(excluido=False)
    template_name = 'aluno_list.html'


class AlunoDetailView(DetailView):
    '''
    Exibe, *atualiza* e `deleta` uma Atividade específica.

    :URL: http://<ip_servidor>/atividade/atividade/<id>/
    '''

    queryset = Aluno.objects.filter(excluido=False)
    template_name = 'aluno_detail.html'
