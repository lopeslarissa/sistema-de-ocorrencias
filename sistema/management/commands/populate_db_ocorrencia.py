# coding: utf-8
"""Populate"""
from datetime import datetime
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from sistema.models.professor import Professor
from sistema.models.aluno import Aluno
from sistema.models.ocorrencia import Ocorrencia


class Command(BaseCommand):
    """Populate Banco Ocorrência"""
    args = u'Nenhum argumento necessário'
    help = u'populate para a base do sistema Ocorrência'

    def _crete_admin(self):
        admin1, created = User.objects.get_or_create(username=u'admin',
                                                     is_superuser=True,
                                                     is_staff=True)
        admin1.set_password(u'admin123')
        admin1.save()

    def _create_ocorrencia(self):
        administrador1, created = Professor.objects.get_or_create(first_name=u'Administrador',
                                                                  last_name=u'do Sistema',
                                                                  email=u'admin@gmail.com',
                                                                  username=u'administrador',
                                                                  is_superuser=True,
                                                                  is_staff=True, )
        administrador1.set_password(u'admin')
        administrador1.save()

        professor1, created = Professor.objects.get_or_create(first_name=u'João',
                                                              last_name=u'Lopes',
                                                              email=u'joao@gmail.com',
                                                              username=u'joao', )
        professor1.set_password(u'joao')
        professor1.save()

        professor2, created = Professor.objects.get_or_create(first_name=u'Marco',
                                                              last_name=u'André',
                                                              email=u'marco@gmail.com',
                                                              username=u'marco', )
        professor2.set_password(u'marco')
        professor2.save()

        professor3, created = Professor.objects.get_or_create(first_name=u'Larissa',
                                                              last_name=u'Lopes',
                                                              email=u'larissa@gmail.com',
                                                              username=u'larissa', )
        professor3.set_password(u'larissa')
        professor3.save()

        aluno1, created = Aluno.objects.get_or_create(nome=u'Natália Caroline',
                                                      email=u'natalia@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'BSI1',
                                                      curso=u'BSI',
                                                      matricula=u'12534', )
        aluno1.save()

        aluno2, created = Aluno.objects.get_or_create(nome=u'Alisson Vinícius',
                                                      email=u'alisson@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'BSI3',
                                                      curso=u'BSI',
                                                      matricula=u'23245', )
        aluno2.save()

        aluno3, created = Aluno.objects.get_or_create(nome=u'Fernanda Carolina',
                                                      email=u'fernanda@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'MedVet',
                                                      curso=u'MedVet1',
                                                      matricula=u'34586', )
        aluno3.save()

        aluno4, created = Aluno.objects.get_or_create(nome=u'Maria Eduarda',
                                                      email=u'maria@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'BSI5',
                                                      curso=u'BSI',
                                                      matricula=u'46567', )
        aluno4.save()

        aluno5, created = Aluno.objects.get_or_create(nome=u'Josué de Borba',
                                                      email=u'josue@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'LICA3',
                                                      curso=u'LICA',
                                                      matricula=u'56478', )
        aluno5.save()

        aluno6, created = Aluno.objects.get_or_create(nome=u'Tiago de Borba',
                                                      email=u'tiago@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'BSI7',
                                                      curso=u'BSI',
                                                      matricula=u'67889', )
        aluno6.save()

        aluno7, created = Aluno.objects.get_or_create(nome=u'João Guilherme',
                                                      email=u'joao@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'LIQUI6',
                                                      curso=u'LIQUI',
                                                      matricula=u'78891', )
        aluno7.save()

        aluno8, created = Aluno.objects.get_or_create(nome=u'Aline Cristina',
                                                      email=u'aline@gmail.com',
                                                      telefone=u'47123456789',
                                                      turma=u'LICA3',
                                                      curso=u'LICA',
                                                      matricula=u'89192', )
        aluno8.save()

        ocorrencia1, created = Ocorrencia.objects.get_or_create(
            professor=professor1,
            aluno=aluno1,
            disciplina=u'Matemática',
            descricao=u'Aluno faltou mais de 3 dias seguidos',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia1.save()

        ocorrencia2, created = Ocorrencia.objects.get_or_create(
            professor=professor2,
            aluno=aluno2,
            disciplina=u'Português',
            descricao=u'Aluno atrapalhou a aula',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia2.save()

        ocorrencia3, created = Ocorrencia.objects.get_or_create(
            professor=professor3,
            aluno=aluno3,
            disciplina=u'Biologia',
            descricao=u'Aluno brigou com outro aluno durante a aula',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia3.save()

        ocorrencia4, created = Ocorrencia.objects.get_or_create(
            professor=professor1,
            aluno=aluno4,
            disciplina=u'Banco de Dados',
            descricao=u'Aluno dormiu em sala de aula',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia4.save()

        ocorrencia5, created = Ocorrencia.objects.get_or_create(
            professor=professor2,
            aluno=aluno5,
            disciplina=u'Biologia',
            descricao=u'Aluno desistiu da matéria',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia5.save()

        ocorrencia6, created = Ocorrencia.objects.get_or_create(
            professor=professor3,
            aluno=aluno6,
            disciplina=u'Química',
            descricao=u'Aluno desistiu da matéria',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia6.save()

        ocorrencia7, created = Ocorrencia.objects.get_or_create(
            professor=professor1,
            aluno=aluno7,
            disciplina=u'Física',
            descricao=u'Aluno faltou',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia7.save()

    def handle(self, *args, **options):
        self._crete_admin()
        self._create_ocorrencia()
