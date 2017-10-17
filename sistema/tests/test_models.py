# # coding=utf-8
# from django.test import TestCase
# from sistema.models.ocorrencia import Ocorrencia
# from sistema.models.professor import Professor
# from sistema.models.aluno import Aluno
# from django.utils import timezone
#
#
# class AlunoTest(TestCase):
#     def create_aluno(self, nome=u'Maria', email=u'maria@gmail.com', telefone='4799082190', turma='BSI6', curso='BSI',
#                      matricula='2565874'):
#         return Aluno.objects.create(nome=nome, email=email, telefone=telefone, turma=turma, curso=curso,
#                                     matricula=matricula)
#
#     def test_aluno_creation(self):
#         aluno = self.create_aluno()
#         self.assertTrue(isinstance(aluno, Aluno))
#         self.assertEqual(aluno.__unicode__(), aluno.nome)
#
#
# class ProfessorTest(TestCase):
#     def create_professor(self, first_name=u'Natália', last_name=u'Caroline', email=u'natalia@gmail.com',
#                          password='1234', username='dinda'):
#         return Professor.objects.create(first_name=first_name, last_name=last_name, email=email, password=password,
#                                         username=username)
#
#     def test_professor_creation(self):
#         professor = self.create_professor()
#         self.assertTrue(isinstance(professor, Professor))
#         self.assertEqual(professor.__unicode__(), professor.first_name)
#
#
# class OcorrenciaTest(TestCase):
#     professor = Professor.objects.create(first_name=u'Natália', last_name=u'Caroline', email=u'natalia@gmail.com',
#                                          password='1234', username=u'olivia')
#     aluno = Aluno.objects.create(nome=u'Maria', email=u'maria@gmail.com', telefone='4799082190', turma='BSI6',
#                                  curso='BSI',
#                                  matricula='2565874')
#
#     def create_ocorrencia(self, aluno=aluno, professor=professor, disciplina=u'matemática',
#                           descricao=u'aluno chegou atrasado', data=timezone.datetime.today(), hora=timezone.now()):
#         return Ocorrencia.objects.create(aluno=aluno, professor=professor, disciplina=disciplina,
#                                          descricao=descricao, data=data, hora=hora)
#
#     def test_ocorrencia_creation(self):
#         ocorrencia = self.create_ocorrencia()
#         self.assertTrue(isinstance(ocorrencia, Ocorrencia))
#         self.assertEqual(ocorrencia.__unicode__(), ocorrencia.descricao)
