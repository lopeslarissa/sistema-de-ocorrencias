from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from sistema.models.professor import Professor
from sistema.models.aluno import Aluno
from sistema.models.ocorrencia import Ocorrencia
from datetime import datetime


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _crete_admin(self):
        admin1 = User(username='admin',
                      is_superuser=True,
                      is_staff=True)
        admin1.set_password('admin123')
        admin1.save()

    def _create_professor(self):
        administrador1 = Professor(first_name='Administrador',
                                   last_name='do Sistema',
                                   email='admin@gmail.com',
                                   username='administrador',
                                   is_superuser=True,
                                   is_staff=True, )
        administrador1.set_password('admin')
        administrador1.save()

        professor1 = Professor(first_name='João',
                               last_name='Lopes',
                               email='joao@gmail.com',
                               username='joao',)
        professor1.set_password('joao')
        professor1.save()

        professor2 = Professor(first_name='Marco',
                               last_name='André',
                               email='marco@gmail.com',
                               username='marco', )
        professor2.set_password('marco')
        professor2.save()

        professor3 = Professor(first_name='Larissa',
                               last_name='Lopes',
                               email='larissa@gmail.com',
                               username='larissa', )
        professor3.set_password('larissa')
        professor3.save()


    def _create_aluno(self):
        aluno1 = Aluno(nome='Natália Caroline',
                       email='natalia@gmail.com',
                       telefone='47123456789',
                       turma='BSI1',
                       curso='BSI',
                       matricula='1234',)
        aluno1.save()

        aluno2 = Aluno(nome='Alisson Vinícius',
                       email='alisson@gmail.com',
                       telefone='47123456789',
                       turma='BSI3',
                       curso='BSI',
                       matricula='2345', )
        aluno2.save()

        aluno3 = Aluno(nome='Fernanda Carolina',
                       email='fernanda@gmail.com',
                       telefone='47123456789',
                       turma='MedVet',
                       curso='MedVet1',
                       matricula='3456', )
        aluno3.save()

        aluno4 = Aluno(nome='Maria Eduarda',
                       email='maria@gmail.com',
                       telefone='47123456789',
                       turma='BSI5',
                       curso='BSI',
                       matricula='4567', )
        aluno4.save()

        aluno5 = Aluno(nome='Josué de Borba',
                       email='josue@gmail.com',
                       telefone='47123456789',
                       turma='LICA3',
                       curso='LICA',
                       matricula='5678', )
        aluno5.save()

        aluno6 = Aluno(nome='Tiago de Borba',
                       email='tiago@gmail.com',
                       telefone='47123456789',
                       turma='BSI7',
                       curso='BSI',
                       matricula='6789', )
        aluno6.save()

        aluno7 = Aluno(nome='João Guilherme',
                       email='joao@gmail.com',
                       telefone='47123456789',
                       turma='LIQUI6',
                       curso='LIQUI',
                       matricula='7891', )
        aluno7.save()

        aluno8 = Aluno(nome='Aline Cristina',
                       email='aline@gmail.com',
                       telefone='47123456789',
                       turma='LICA3',
                       curso='LICA',
                       matricula='8912', )
        aluno8.save()

    def _create_ocorrencia(self):
        ocorrencia1 = Ocorrencia(professor=Professor.objects.get(pk=3),
                                 aluno=Aluno.objects.get(pk=1),
                                 disciplina= 'Matemática',
                                 descricao='Aluno faltou mais de 3 dias seguidos',
                                 hora=datetime.now().time(),
                                 data=datetime.now().date(),)
        ocorrencia1.save()

        ocorrencia2 = Ocorrencia(professor=Professor.objects.get(pk=2),
                                 aluno=Aluno.objects.get(pk=2),
                                 disciplina='Português',
                                 descricao='Aluno atrapalhou a aula',
                                 hora=datetime.now().time(),
                                 data=datetime.now().date(),)
        ocorrencia2.save()

        ocorrencia3 = Ocorrencia(professor=Professor.objects.get(pk=3),
                                 aluno=Aluno.objects.get(pk=3),
                                 disciplina='Biologia',
                                 descricao='Aluno brigou com outro aluno durante a aula',
                                 hora=datetime.now().time(),
                                 data=datetime.now().date(), )
        ocorrencia3.save()

        ocorrencia4 = Ocorrencia(professor=Professor.objects.get(pk=2),
                                 aluno=Aluno.objects.get(pk=4),
                                 disciplina='Banco de Dados',
                                 descricao='Aluno dormiu em sala de aula',
                                 hora=datetime.now().time(),
                                 data=datetime.now().date(), )
        ocorrencia4.save()

        ocorrencia5 = Ocorrencia(professor=Professor.objects.get(pk=2),
                                 aluno=Aluno.objects.get(pk=5),
                                 disciplina='Biologia',
                                 descricao='Aluno desistiu da matéria',
                                 hora=datetime.now().time(),
                                 data=datetime.now().date(), )
        ocorrencia5.save()

    def handle(self, *args, **options):
        self._crete_admin()
        self._create_professor()
        self._create_aluno()
        self._create_ocorrencia()
