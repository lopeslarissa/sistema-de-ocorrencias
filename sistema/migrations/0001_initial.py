# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, verbose_name=b'E-mail')),
                ('telefone', models.CharField(max_length=11)),
                ('turma', models.CharField(max_length=250)),
                ('curso', models.CharField(max_length=250)),
                ('matricula', models.CharField(max_length=250)),
                ('excluido', models.BooleanField(verbose_name=b'Exclu\xc3\xaddo')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_professor', models.CharField(max_length=250, verbose_name=b'Nome do Professor', blank=True)),
                ('nome_aluno', models.CharField(max_length=250, verbose_name=b'Nome do Aluno')),
                ('disciplina', models.CharField(max_length=250)),
                ('descricao', models.TextField(max_length=1000, verbose_name=b'Descri\xc3\xa7\xc3\xa3o da ocorr\xc3\xaancia')),
                ('turma', models.CharField(max_length=250, blank=True)),
                ('matricula', models.CharField(max_length=250, verbose_name=b'Matr\xc3\xadcula', blank=True)),
                ('hora', models.TimeField()),
                ('data', models.DateField()),
                ('excluido', models.BooleanField(verbose_name=b'Exclu\xc3\xaddo')),
            ],
            options={
                'verbose_name': 'Ocorr\xeancia',
                'verbose_name_plural': 'Ocorr\xeancias',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
