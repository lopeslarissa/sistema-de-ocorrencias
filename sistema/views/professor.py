# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.shortcuts import render
from sistema.forms.professor import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.core.urlresolvers import reverse_lazy


template = 'cadastrar_professor.html'
template2 = 'home.html'
template3 = 'index.html'
template4 = 'alterar_status.html'


class CadastraProfessor(View):
    def get(self, request):
        id = request.user.id
        if id:
            print(id)
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
                return render(request, template3, {'form': LoginForm})
            else:
                print(form.errors)
            return render(request, template, {'form': ProfessorForm})


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, template3, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if Professor.objects.filter(username=username):
                login(request, user)
                context_dict = {'msg': "Login efetuado com sucesso!"}
                return render(request, template2, context_dict)
            else:
                return render(request, template4, {"msg": "Conta inativa, deseja ativar?", 'form':LoginForm})
        else:
            return render(request, template3, {"msg": "Senha ou login errados", 'form':LoginForm})


# @method_decorator(login_required(login_url='/sistema/'))
class AlterarStatus(View):
    def get(self, request):
        return render(request, template4, {'form': LoginForm})

    def post(self, request):
        if request.user.id:
            ativo = Professor.objects.get(username=request.user.username)
            ativo.is_active = False
            ativo.save()
            logout(request)
            return redirect('/sistema/')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                ativo = Professor.objects.get(username=user.username)
                if ativo.is_active is False:
                    ativo.is_active = True
                    ativo.save()
                    return render(request, template3, {'msg': 'usuario ativado com sucesso!', 'form': LoginForm})
                else:
                    return render(request, template3, {'msg': 'Este usuario já esta ativo', 'form': LoginForm})
            else:
                return render(request, template4, {'msg': 'Usuario ou senha incorretos', 'form': LoginForm})