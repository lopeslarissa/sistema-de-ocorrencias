# coding=utf-8
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from sistema.forms.aluno import *
from sistema.models.ocorrencia import Ocorrencia

template = 'cadastrar_aluno.html'
template2 = 'index.html'
template3 = 'aluno.html'


class CadastraAluno(View):
    def get(self, request, id=None):
        if request.user.is_authenticated:
            if id:
                aluno = Aluno.objects.get(pk=id)
                form = AlunoForm(instance=aluno)
                return render(request, template, {'form': form, 'id': id})
            else:
                form = AlunoForm()
                return render(request, template, {'form': form})
        else:
            return HttpResponseRedirect('login')

    def post(self, request, id=None):
        if request.user.is_authenticated:
            if id:
                aluno = Aluno.objects.get(pk=id)
                form = AlunoForm(instance=aluno, data=request.POST)
                if form.is_valid():
                    aluno = form.save(commit=False)
                    aluno.excluido = False
                    aluno.save()
                    return render(request, template3, {'msg': 'Aluno Alterado com Sucesso!', 'aluno': aluno})
                else:
                    print(form.errors)
                return render(request, template, {'form': AlunoForm})
            else:
                form = AlunoForm(data=request.POST)
                if form.is_valid():
                    aluno = form.save(commit=False)
                    aluno.excluido = False
                    aluno.save()
                    return render(request, template3, {'msg': 'Aluno Cadastrado com Sucesso!', 'aluno': aluno})
                else:
                    print(form.errors)
            return render(request, template, {'form': AlunoForm})
        else:
            return HttpResponseRedirect('login')

class ExcluirAluno(View):
    def post(self, request, id=None):
        if request.user.is_authenticated:
            aluno = Aluno.objects.get(pk=id)
            aluno.excluido = True
            aluno.save()
            return ListarObjetos(request)
        else:
            return HttpResponseRedirect('login')


def ListarObjetos(request):
    if request.user.is_authenticated:
        context_dict = {}
        alunos = Aluno.objects.all().exclude(excluido=True)
        ocorrencias = Ocorrencia.objects.all().exclude(excluido=True)
        context_dict['alunos'] = alunos
        context_dict['ocorrencias'] = ocorrencias
        return render(request, template2, context_dict)
    else:
        return HttpResponseRedirect('login')


class DetalharAluno(View):
    def get(self, request, id=None):
        if request.user.is_authenticated:
            aluno = Aluno.objects.get(pk=id)
            context_dict = {'aluno': aluno}
            return render(request, template3, context_dict)
        else:
            return HttpResponseRedirect('login')