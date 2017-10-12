# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.urls import reverse


class Professor(User):
    """
    Model abstrata do django
    """

    def __unicode__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('professor-update')

    class Meta:
        app_label = 'sistema'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'