from django.conf.urls import url
from django.views.generic import TemplateView
from sistema.views.aluno import *
from sistema.views.professor import *
from sistema.views.ocorrencia import *

urlpatterns = [
    url(r'^excluir-aluno/(?P<id>\d+)/$', ExcluirAluno.as_view(), name='excluir-aluno'),
    url(r'^cadastrar-aluno/$', CadastraAluno.as_view(), name='cadastrar-aluno'),
    url(r'^editar-aluno/(?P<id>\d+)/$', CadastraAluno.as_view(), name='editar-aluno'),
    url(r'^aluno/(?P<id>\d+)/$', DetalharAluno, name='aluno'),

    url(r'^excluir-ocorrencia/(?P<id>\d+)/$', ExcluirOcorrencia.as_view(), name='excluir-ocorrencia'),
    url(r'^cadastrar-ocorrencia/$', CadastraOcorrencia.as_view(), name='cadastrar-ocorrencia'),
    url(r'^editar-ocorrencia/(?P<id>\d+)/$', CadastraOcorrencia.as_view(), name='editar-ocorrencia'),
    url(r'^ocorrencia/(?P<id>\d+)/$', DetalharOcorrencia.as_view(), name='ocorrencia'),

    url(r'^conta-professor/$', AlterarStatus.as_view, name='alterar-status'),
    url(r'^cadastrar-professor/$', CadastraProfessor.as_view(), name='cadastrar-professor'),
    url(r'^editar-professor/$', CadastraProfessor.as_view(), name='editar-professor'),
    url(r'', Login.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/sistema/'}, name='logout'),

    url(r'^home/$', ListarObjetos.as_view(), name='home'),
    # url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
