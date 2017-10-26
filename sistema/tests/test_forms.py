# coding=utf-8
"""Teste de Formulário"""
from django.test import TestCase
from sistema.forms.aluno import AlunoForm
from sistema.models.aluno import Aluno


class AlunoFormTest(TestCase):
    """Teste de Formulário de Aluno"""
    def test_valid_form(self):
        """Teste de formulário válido de Aluno"""
        aluno = Aluno.objects.create(nome=u'Maria',
                                     email=u'maria@gmail.com',
                                     telefone='4799082190',
                                     turma='BSI6',
                                     curso='BSI',
                                     matricula='2565874')
        data = {'nome': aluno.nome,
                'email': aluno.email,
                'telefone': aluno.telefone,
                'turma': aluno.turma,
                'curso': aluno.curso,
                'matricula': aluno.matricula, }
        form = AlunoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Teste de formulário válido de Aluno"""
        aluno = Aluno.objects.create(nome=u'Maria',
                                     email=u'',
                                     telefone='',
                                     turma='BSI6',
                                     curso='BSI',
                                     matricula='')
        data = {'nome': aluno.nome,
                'email': aluno.email,
                'telefone': aluno.telefone,
                'turma': aluno.turma,
                'curso': aluno.curso,
                'matricula': aluno.matricula, }
        form = AlunoForm(data=data)
        self.assertFalse(form.is_valid())
