# -*- coding: utf-8 -*-
from django.contrib.auth.models import User


class Professor(User):

    def __unicode__(self):
        return self.first_name

    class Meta:
        app_label = 'sistema'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'