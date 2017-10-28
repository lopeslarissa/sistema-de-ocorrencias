# coding=utf-8
"""Teste de Model"""
from django.utils import timezone
from django.test import TestCase
from sistema.models.ocorrencia import Ocorrencia
from sistema.models.professor import Professor
from sistema.models.aluno import Aluno


class AlunoTest(TestCase):
    """Teste de Model de Aluno"""
    def create_aluno(self,
                     nome=u'Maria',
                     email=u'maria@gmail.com',
                     telefone='4799082190',
                     turma='BSI6',
                     curso='BSI',
                     matricula='2565874'):
        """Método que cria aluno"""
        return Aluno.objects.create(nome=nome,
                                    email=email,
                                    telefone=telefone,
                                    turma=turma,
                                    curso=curso,
                                    matricula=matricula)

    def test_aluno_creation(self):
        """Método que testa a criação de aluno"""
        aluno = self.create_aluno()
        self.assertTrue(isinstance(aluno, Aluno))
        self.assertEqual(aluno.__unicode__(), aluno.nome)


class ProfessorTest(TestCase):
    """Teste de Model de Professor"""
    def create_professor(self,
                         first_name=u'Natália',
                         last_name=u'Caroline',
                         email=u'natalia@gmail.com',
                         password='1234',
                         username='dinda'):
        """Método que cria professor"""
        return Professor.objects.create(first_name=first_name,
                                        last_name=last_name,
                                        email=email,
                                        password=password,
                                        username=username)

    def test_professor_creation(self):
        """Método que testa a criação de professor"""
        professor = self.create_professor()
        self.assertTrue(isinstance(professor, Professor))
        self.assertEqual(professor.__unicode__(), professor.first_name)


class OcorrenciaTest(TestCase):
    """Teste de Model de Ocorrência"""
    professor = Professor.objects.create(first_name=u'Natália',
                                         last_name=u'Caroline',
                                         email=u'natalia@gmail.com',
                                         password='1234',
                                         username=u'olivia')
    aluno = Aluno.objects.create(nome=u'Maria',
                                 email=u'maria@gmail.com',
                                 telefone='4799082190',
                                 turma='BSI6',
                                 curso='BSI',
                                 matricula='2565874')

    def create_ocorrencia(self,
                          aluno=aluno,
                          professor=professor,
                          disciplina=u'matemática',
                          descricao=u'aluno chegou atrasado',
                          data=timezone.datetime.today(),
                          hora=timezone.now()):
        """Método que cria ocorrencia"""
        return Ocorrencia.objects.create(aluno=aluno,
                                         professor=professor,
                                         disciplina=disciplina,
                                         descricao=descricao,
                                         data=data,
                                         hora=hora)

    def test_ocorrencia_creation(self):
        """Método que testa a criação de ocorrêcia"""
        ocorrencia = self.create_ocorrencia()
        self.assertTrue(isinstance(ocorrencia, Ocorrencia))
        self.assertEqual(ocorrencia.__unicode__(), ocorrencia.descricao)
