from django.db import models
from django.utils.translation import ugettext_lazy as _


class Agile(models.Model):
    name = models.CharField(_('agile value name'), max_length=100)
    description = models.TextField(_('agile value description'),
                    blank=True,
                    default='',
                    help_text='Description of the Agile Value.')

    creation_date = models.DateTimeField(_('date created'), auto_now_add=True)
    modified_date = models.DateTimeField(_('date last modified'), auto_now=True)

    class Meta:
        verbose_name_plural = _('Agile Values')


    def __str__(self):
        return f'{self.name}'


class Principle(models.Model):
    name = models.CharField(_('principle name'), max_length=100)
    description = models.TextField(_('principle description'),
                    blank=True,
                    default='',
                    help_text='Description of the Agile Principle.')

    creation_date = models.DateTimeField(_('date created'), auto_now_add=True)
    modified_date = models.DateTimeField(_('date last modified'), auto_now=True)

    class Meta:
        verbose_name_plural = _('Principles')


    def __str__(self):
        return f'{self.name}'
