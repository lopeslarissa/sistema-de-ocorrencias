# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from sistema.forms.ocorrencia import *
from sistema.models.professor import Professor

template = 'cadastrar_ocorrencia.html'
template2 = 'ocorrencia/'


# @method_decorator(login_required(login_url='/sistema/'))
class CadastraOcorrencia(View):
    def get(self, request, id = None):
        if id:
            ocorrencia = Ocorrencia.objects.get(pk=id)
            form = OcorrenciaForm(instance=ocorrencia)
        else:
            form = OcorrenciaForm()
        return render(request, template, {'form': form})

    def post(self, request, id = None):
        if id:
            ocorrencia = Ocorrencia.objects.get(pk=id)
            form = OcorrenciaForm(instance=ocorrencia, data=request.POST)
            if form.is_valid():
                ocorrencia = form.save(commit=False)
                professor = Professor.objects.get(pk=request.user.id)
                ocorrencia.professor = professor
                ocorrencia.save()
                return redirect(template2 + str(ocorrencia.id)+'/')
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
                return render(request, template2 + str(ocorrencia.id) + '/', {'msg': 'Ocorrência Cadastrada com Sucesso!'})
            else:
                print(form.errors)
        return render(request, template, {'form': form})


class ExcluirOcorrencia(View):
    def get(self, request, id=None):
        ocorrencia = Ocorrencia.objects.get(pk=id)
        ocorrencia.excluido = True
        ocorrencia.save()
        return render(request, template2 + str(ocorrencia.id) + '/')


# @method_decorator(login_required(login_url='/sistema/'))
class DetalharOcorrencia(View):
    def get(self, request, id=None):
        ocorrencia = Ocorrencia.objects.get(pk=id)
        context_dict = {'ocorrencia': ocorrencia}
        return render(request, template2, context_dict)

