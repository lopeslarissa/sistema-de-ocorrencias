# coding=utf-8
from django.test import TestCase

from sistema.forms.professor import ProfessorForm
from sistema.forms.ocorrencia import OcorrenciaForm
from sistema.forms.aluno import AlunoForm
from sistema.models.ocorrencia import Ocorrencia
from sistema.models.professor import Professor
from sistema.models.aluno import Aluno
from django.utils import timezone


class AlunoFormTest(TestCase):
    def test_valid_form(self):
        aluno = Aluno.objects.create(nome=u'Maria', email=u'maria@gmail.com', telefone='4799082190', turma='BSI6',
                                     curso='BSI', matricula='2565874')
        data = {'nome': aluno.nome, 'email': aluno.email, 'telefone': aluno.telefone, 'turma': aluno.turma,
                'curso': aluno.curso, 'matricula': aluno.matricula, }
        form = AlunoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        aluno = Aluno.objects.create(nome=u'Maria', email=u'', telefone='', turma='BSI6', curso='BSI',
                                     matricula='')
        data = {'nome': aluno.nome, 'email': aluno.email, 'telefone': aluno.telefone, 'turma': aluno.turma,
                'curso': aluno.curso, 'matricula': aluno.matricula, }
        form = AlunoForm(data=data)
        self.assertFalse(form.is_valid())


class ProfessorFormTest(TestCase):
    def test_valid_form(self):
        professor = Professor.objects.create(first_name=u'Natália', last_name=u'Caroline',
                                             email=u'natalia@gmail.com', password='1234', username='benta')
        data = {'first_name': professor.first_name, 'last_name': professor.last_name, 'email': professor.email,
                'password': professor.password, 'username': professor.username, }
        form = ProfessorForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        professor = Professor.objects.create(first_name=u'', last_name=u'Caroline', email=u'',
                                             password='1234', username='')
        data = {'first_name': professor.first_name, 'last_name': professor.last_name, 'email': professor.email,
                'password': professor.password, 'username': professor.username, }
        form = ProfessorForm(data=data)
        self.assertFalse(form.is_valid())


class OcorrenciaFormTest(TestCase):
    def test_valid_form(self):
        professor = Professor.objects.create(first_name=u'Natália', last_name=u'Caroline',
                                             email=u'natalia@gmail.com', password='1234', username='beti')

        aluno = Aluno.objects.create(nome=u'Maria', email=u'maria@gmail.com', telefone='4799082190', turma='BSI6',
                                     curso='BSI', matricula='2565874')

        ocorrencia = Ocorrencia.objects.create(aluno=aluno, professor=professor, disciplina=u'matemática',
                                               descricao=u'aluno chegou atrasado', data=timezone.datetime.today(),
                                               hora=timezone.now())

        data = {'aluno': ocorrencia.aluno, 'professor': ocorrencia.professor, 'disciplina': ocorrencia.disciplina,
                'descricao': ocorrencia.descricao, 'data': ocorrencia.data,
                'hora': ocorrencia.hora, }
        form = OcorrenciaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        professor = Professor.objects.create(first_name=u'Natália', last_name=u'Caroline',
                                             email=u'natalia@gmail.com', password='1234', username='ana')

        aluno = Aluno.objects.create(nome=u'Maria', email=u'maria@gmail.com', telefone='4799082190', turma='BSI6',
                                     curso='BSI', matricula='2565874')

        ocorrencia = Ocorrencia.objects.create(aluno=aluno, professor=professor, disciplina=u'',
                                               descricao=u'', data='',
                                               hora=timezone.now())

        data = {'aluno': ocorrencia.aluno, 'professor': ocorrencia.professor, 'disciplina': ocorrencia.disciplina,
                'descricao': ocorrencia.descricao, 'data': ocorrencia.data,
                'hora': ocorrencia.hora, }
        form = OcorrenciaForm(data=data)
        self.assertFalse(form.is_valid())
