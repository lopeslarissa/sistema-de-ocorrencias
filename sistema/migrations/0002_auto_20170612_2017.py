# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrencia',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='nome_aluno',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='nome_professor',
        ),
        migrations.RemoveField(
            model_name='ocorrencia',
            name='turma',
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='aluno',
            field=models.ManyToManyField(to='sistema.Aluno'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='professor',
            field=models.ForeignKey(default=1, blank=True, to='sistema.Professor'),
            preserve_default=False,
        ),
    ]
