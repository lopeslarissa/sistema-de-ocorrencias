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
        admin1, created = User.objects.get_or_create(username='admin',
                                                     is_superuser=True,
                                                     is_staff=True)
        admin1.set_password('admin123')
        admin1.save()

    def _create_ocorrencia(self):
        administrador1, created = Professor.objects.get_or_create(first_name='Administrador',
                                                                  last_name='do Sistema',
                                                                  email='admin@gmail.com',
                                                                  username='administrador',
                                                                  is_superuser=True,
                                                                  is_staff=True, )
        administrador1.set_password('admin')
        administrador1.save()

        professor1, created = Professor.objects.get_or_create(first_name='João',
                                                              last_name='Lopes',
                                                              email='joao@gmail.com',
                                                              username='joao', )
        professor1.set_password('joao')
        professor1.save()

        professor2, created = Professor.objects.get_or_create(first_name='Marco',
                                                              last_name='André',
                                                              email='marco@gmail.com',
                                                              username='marco', )
        professor2.set_password('marco')
        professor2.save()

        professor3, created = Professor.objects.get_or_create(first_name='Larissa',
                                                              last_name='Lopes',
                                                              email='larissa@gmail.com',
                                                              username='larissa', )
        professor3.set_password('larissa')
        professor3.save()

        aluno1, created = Aluno.objects.get_or_create(nome='Natália Caroline',
                                                      email='natalia@gmail.com',
                                                      telefone='47123456789',
                                                      turma='BSI1',
                                                      curso='BSI',
                                                      matricula='12534', )
        aluno1.save()

        aluno2, created = Aluno.objects.get_or_create(nome='Alisson Vinícius',
                                                      email='alisson@gmail.com',
                                                      telefone='47123456789',
                                                      turma='BSI3',
                                                      curso='BSI',
                                                      matricula='23245', )
        aluno2.save()

        aluno3, created = Aluno.objects.get_or_create(nome='Fernanda Carolina',
                                                      email='fernanda@gmail.com',
                                                      telefone='47123456789',
                                                      turma='MedVet',
                                                      curso='MedVet1',
                                                      matricula='34586', )
        aluno3.save()

        aluno4, created = Aluno.objects.get_or_create(nome='Maria Eduarda',
                                                      email='maria@gmail.com',
                                                      telefone='47123456789',
                                                      turma='BSI5',
                                                      curso='BSI',
                                                      matricula='46567', )
        aluno4.save()

        aluno5, created = Aluno.objects.get_or_create(nome='Josué de Borba',
                                                      email='josue@gmail.com',
                                                      telefone='47123456789',
                                                      turma='LICA3',
                                                      curso='LICA',
                                                      matricula='56478', )
        aluno5.save()

        aluno6, created = Aluno.objects.get_or_create(nome='Tiago de Borba',
                                                      email='tiago@gmail.com',
                                                      telefone='47123456789',
                                                      turma='BSI7',
                                                      curso='BSI',
                                                      matricula='67889', )
        aluno6.save()

        aluno7, created = Aluno.objects.get_or_create(nome='João Guilherme',
                                                      email='joao@gmail.com',
                                                      telefone='47123456789',
                                                      turma='LIQUI6',
                                                      curso='LIQUI',
                                                      matricula='78891', )
        aluno7.save()

        aluno8, created = Aluno.objects.get_or_create(nome='Aline Cristina',
                                                      email='aline@gmail.com',
                                                      telefone='47123456789',
                                                      turma='LICA3',
                                                      curso='LICA',
                                                      matricula='89192', )
        aluno8.save()

        ocorrencia1, created = Ocorrencia.objects.get_or_create(
            professor=professor1,
            aluno=aluno1,
            disciplina='Matemática',
            descricao='Aluno faltou mais de 3 dias seguidos',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia1.save()

        ocorrencia2, created = Ocorrencia.objects.get_or_create(
            professor=professor2,
            aluno=aluno2,
            disciplina='Português',
            descricao='Aluno atrapalhou a aula',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia2.save()

        ocorrencia3, created = Ocorrencia.objects.get_or_create(
            professor=professor3,
            aluno=aluno3,
            disciplina='Biologia',
            descricao='Aluno brigou com outro aluno durante a aula',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia3.save()

        ocorrencia4, created = Ocorrencia.objects.get_or_create(
            professor=professor1,
            aluno=aluno4,
            disciplina='Banco de Dados',
            descricao='Aluno dormiu em sala de aula',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia4.save()

        ocorrencia5, created = Ocorrencia.objects.get_or_create(
            professor=professor2,
            aluno=aluno5,
            disciplina='Biologia',
            descricao='Aluno desistiu da matéria',
            hora=datetime.now().time(),
            data=datetime.now().date(), )
        ocorrencia5.save()

    def handle(self, *args, **options):
        self._crete_admin()
        self._create_ocorrencia()
