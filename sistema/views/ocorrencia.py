# coding=utf-8
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sistema.forms.ocorrencia import *
from sistema.models.professor import Professor
from sistema.views import ListarObjetos

template = 'cadastrar_ocorrencia.html'
template2 = 'ocorrencia.html'
template3 = 'index.html'


class CadastraOcorrencia(View):
    def get(self, request, id = None):
        if request.user.is_authenticated:
            if id:
                ocorrencia = Ocorrencia.objects.get(pk=id)
                form = OcorrenciaForm(instance=ocorrencia)
                return render(request, template, {'form': form, 'id': id})
            else:
                form = OcorrenciaForm()
                return render(request, template, {'form': form})
        else:
            return HttpResponseRedirect(reverse('index'))

    def post(self, request, id = None):
        if request.user.is_authenticated:
            if id:
                ocorrencia_bd = Ocorrencia.objects.get(pk=id)
                form = OcorrenciaForm(instance=ocorrencia_bd, data=request.POST )
                if form.is_valid():
                    professor = Professor.objects.get(pk=request.user.id)
                    ocorrencia = form.save(commit=False)
                    ocorrencia.professor = professor
                    ocorrencia.save()
                    return render(request, template2, {'msg': 'Ocorrência Alterada com Sucesso!',  'ocorrencia': ocorrencia})
                else:
                    print(form.errors)
                    return render(request, template, {'form': form})
            else:
                form = OcorrenciaForm(data=request.POST)
                if form.is_valid():
                    ocorrencia = form.save(commit=False)
                    professor = Professor.objects.get(pk=request.user.id)
                    ocorrencia.professor = professor
                    ocorrencia.save()
                    return render(request, template2, {'msg': 'Ocorrência Cadastrada com Sucesso!',  'ocorrencia': ocorrencia})
                else:
                    print(form.errors)
            return render(request, template, {'form': form})
        else:
            return HttpResponseRedirect(reverse('index'))


class ExcluirOcorrencia(View):
    def post(self, request, id=None):
        if request.user.is_authenticated:
            ocorrencia = Ocorrencia.objects.get(pk=id)
            ocorrencia.excluido = True
            ocorrencia.save()
            return ListarObjetos(request)
        else:
            return HttpResponseRedirect(reverse('index'))


class DetalharOcorrencia(View):
    def get(self, request, id=None):
        if request.user.is_authenticated:
            ocorrencia = Ocorrencia.objects.get(pk=id)
            context_dict = {'ocorrencia': ocorrencia}
            return render(request, template2, context_dict)
        else:
            return HttpResponseRedirect(reverse('index'))
