# coding=utf-8
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from sistema.forms.professor import *
from django.http import HttpResponseRedirect


template = 'cadastrar_professor.html'
template2 = 'index.html'


class CadastraProfessor(View):
    def get(self, request):
        id = request.user.id
        if id:
            professor = Professor.objects.get(pk=id)
            form = ProfessorEditForm(instance=professor)
        else:
            form = ProfessorForm
        return render(request, template, {'form': form})

    def post(self, request):
        id = request.user.id
        print(id)
        if id:
            professor = Professor.objects.get(pk=id)
            form = ProfessorEditForm(instance=professor, data=request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.set_password(request.POST['password'])
                form.is_active = True
                form.save()
                user = authenticate(username=professor.username, password=request.POST['password'])
                login(request, user)
                return render(request, template2, {'msg': 'Informações alteradas com sucesso!'})
            else:
                print(form.errors)
            return render(request, template, {'form': ProfessorEditForm})
        else:
            form = ProfessorForm(data=request.POST)
            if form.is_valid():
                professor = form.save(commit=False)
                professor.set_password(request.POST['password'])
                professor.is_active = True
                professor.save()
                return HttpResponseRedirect('login')
            else:
                print(form.errors)
            return render(request, template, {'form': ProfessorForm})


class DesativarProfessor(View):
    def post(self, request):
        if request.user.is_authenticated:
            id = request.user.id
            ativo = Professor.objects.get(pk=id)
            ativo.is_active = False
            ativo.save()
            logout(request)
            return HttpResponseRedirect('login')
        else:
            return HttpResponseRedirect('login')