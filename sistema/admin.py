from django.contrib import admin
from sistema.models.aluno import Aluno
from sistema.models.ocorrencia import Ocorrencia
from sistema.models.professor import Professor

admin.site.register(Aluno)
admin.site.register(Ocorrencia)
admin.site.register(Professor)