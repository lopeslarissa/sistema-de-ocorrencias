from django.conf.urls import url
from django.views.generic import TemplateView
from sistema import views
from sistema.views.aluno import *
from sistema.views.professor import *
from sistema.views.ocorrencia import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^excluir-aluno/(?P<id>\d+)/$', ExcluirAluno.as_view(), name='excluir-aluno'),
    url(r'^cadastrar-aluno/$', CadastraAluno.as_view(), name='cadastrar-aluno'),
    url(r'^editar-aluno/(?P<id>\d+)/$', CadastraAluno.as_view(), name='editar-aluno'),
    url(r'^aluno/(?P<id>\d+)/$', DetalharAluno.as_view(), name='aluno'),

    url(r'^excluir-ocorrencia/(?P<id>\d+)/$', ExcluirOcorrencia.as_view(), name='excluir-ocorrencia'),
    url(r'^cadastrar-ocorrencia/$', CadastraOcorrencia.as_view(), name='cadastrar-ocorrencia'),
    url(r'^editar-ocorrencia/(?P<id>\d+)/$', CadastraOcorrencia.as_view(), name='editar-ocorrencia'),
    url(r'^ocorrencia/(?P<id>\d+)/$', DetalharOcorrencia.as_view(), name='ocorrencia'),

    url(r'^desativar-professor/$', DesativarProfessor.as_view(), name='desativar-professor'),
    url(r'^cadastrar-professor/$', CadastraProfessor.as_view(), name='cadastrar-professor'),
    url(r'^editar-professor/$', CadastraProfessor.as_view(), name='editar-professor'),

    url(r'^login', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout', logout, {'next_page': '/sistema/login/'}, name='logout'),

    url(r'^$', views.ListarObjetos, name='index'),
    url(r'^home/$', views.ListarObjetos, name='index'),
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
