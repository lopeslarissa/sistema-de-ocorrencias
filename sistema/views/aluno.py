# coding=utf-8
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from sistema.forms.aluno import AlunoForm
from sistema.models.aluno import Aluno


class AlunoCreateView(CreateView):
    """
    Cadastra um Aluno.

    :URL: http://<ip_servidor>/cadastrar-aluno/
    """
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = False
        self.object.save()
        return super(AlunoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AlunoCreateView, self).get_context_data(**kwargs)
        context['msg'] = 'Aluno cadastrado com sucesso!'
        return context


class AlunoUpdateView(UpdateView):
    """
    Atualiza os dados do Aluno selecionado.

    :URL: http://<ip_servidor>/editar-aluno/<id>/
    """
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = False
        self.object.save()
        return super(AlunoUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AlunoUpdateView, self).get_context_data(**kwargs)
        context['msg'] = 'Aluno atualizado com sucesso!'
        return context


class AlunoDeleteView(DeleteView):
    """
    Desativa o Aluno selecionado.

    :URL: http://<ip_servidor>/excluir-aluno/<id>/
    """
    queryset = Aluno.objects.filter(excluido=False)
    success_url = reverse_lazy('aluno-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.excluido = True
        self.object.save()
        return super(AlunoDeleteView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AlunoDeleteView, self).get_context_data(**kwargs)
        context['msg'] = 'Aluno deletado com sucesso!'
        return context


class AlunoListView(ListView):
    """
    Lista todos os Alunos, exceto os desativados.

    :URL: http://<ip_servidor>/listar-aluno/
    """
    queryset = Aluno.objects.filter(excluido=False)
    template_name = 'aluno_list.html'


class AlunoDetailView(DetailView):
    """
    Exibe os dados do Aluno selecionado.

    :URL: http://<ip_servidor>/vizualizar-aluno/<id>/
    """
    queryset = Aluno.objects.filter(excluido=False)
    template_name = 'aluno_detail.html'
