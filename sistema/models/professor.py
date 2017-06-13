# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Professor(User):

    def __unicode__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('professor-detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = 'sistema'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'