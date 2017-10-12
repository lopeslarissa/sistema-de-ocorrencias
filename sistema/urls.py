from django.conf.urls import url
from django.views.generic import TemplateView
from sistema import views
from sistema.views.aluno import *
from sistema.views.professor import *
from sistema.views.ocorrencia import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^excluir-aluno/(?P<pk>\d+)/$', AlunoDeleteView.as_view(), name='aluno-delete'),
    url(r'^cadastrar-aluno/$', AlunoCreateView.as_view(), name='aluno-create'),
    url(r'^editar-aluno/(?P<pk>\d+)/$', AlunoUpdateView.as_view(), name='aluno-update'),
    url(r'^vizualizar-aluno/(?P<pk>\d+)/$', AlunoDetailView.as_view(), name='aluno-detail'),
    url(r'^listar-aluno/$', AlunoListView.as_view(), name='aluno-list'),

    url(r'^excluir-ocorrencia/(?P<pk>\d+)/$', OcorrenciaDeleteView.as_view(), name='ocorrencia-delete'),
    url(r'^cadastrar-ocorrencia/$', OcorrenciaCreateView.as_view(), name='ocorrencia-create'),
    url(r'^editar-ocorrencia/(?P<pk>\d+)/$', OcorrenciaUpdateView.as_view(), name='ocorrencia-update'),
    url(r'^vizualizar-ocorrencia/(?P<pk>\d+)/$', OcorrenciaDetailView.as_view(), name='ocorrencia-detail'),
    url(r'^listar-ocorrencia/$', OcorrenciaListView.as_view(), name='ocorrencia-list'),

    url(r'^desativar-professor/$', ProfessorDeleteView.as_view(), name='professor-delete'),
    url(r'^cadastrar-professor/$', ProfessorCreateView.as_view(), name='professor-create'),
    url(r'^editar-professor/$', ProfessorUpdateView.as_view(), name='professor-update'),

    url(r'^login', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout', logout, {'next_page': '/login/'}, name='logout'),

    url(r'^$', OcorrenciaListView.as_view(), name='index'),
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
