# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from sistema.forms.aluno import *
from sistema.models.ocorrencia import Ocorrencia

template = 'cadastrar_aluno.html'
template2 = 'home.html'


# @method_decorator(login_required(login_url='/sistema/'))
class CadastraAluno(View):
    def get(self, request, id=None):
        if id:
            aluno = Aluno.objects.get(pk=id)
            form = AlunoForm(instance=aluno)
        else:
            form = AlunoForm()
        return render(request, template, {'form': form})

    def post(self, request, id=None):
        if id:
            aluno = Aluno.objects.get(pk=id)
            form = AlunoForm(instance=aluno, data=request.POST)
            if form.is_valid():
                aluno = form.save(commit=False)
                aluno.excluido = False
                aluno.save()
                return redirect(template2)
            else:
                print(form.errors)
            return render(request, template, {'form': AlunoForm})
        else:
            form = AlunoForm(data=request.POST)
            if form.is_valid():
                aluno = form.save(commit=False)
                aluno.excluido = False
                aluno.save()
                return render(request, template2, {'msg': 'Aluno Cadastrado com Sucesso!'})
            else:
                print(form.errors)
        return render(request, template, {'form': AlunoForm})


# @method_decorator(login_required(login_url='/sistema/'))
class ExcluirAluno(View):
    def get(self, id=None):
        aluno = Aluno.objects.get(pk=id)
        aluno.excluido = True
        aluno.save()
        return redirect(template2)


# @method_decorator(login_required(login_url='/sistema/'))
class ListarObjetos(View):
    def get(self, request):
        context_dict = {}
        alunos = Aluno.objects.all().exclude(excluido=True)
        ocorrencias = Ocorrencia.objects.all().exclude(excluido=True)
        context_dict['alunos'] = alunos
        context_dict['ocorrencias'] = ocorrencias
        return render(request, template2, context_dict)


# @method_decorator(login_required(login_url='/sistema/'))
class DetalharAluno(View):
    def get(self, request, id=None):
        aluno = Aluno.objects.get(pk=id)
        context_dict = {'aluno': aluno}
        return render(request, 'aluno.html', context_dict)
