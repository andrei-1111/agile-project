from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _


class AgileManager(models.Manager):

    def get_or_none(self, **kwargs):
        """
        Like the standard ``.get()`` except it returns ``None`` rather than
        raising a ``DoesNotExist` exception.
        """
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def get_values(self) -> 'QuerySet[Agile]':
        return self.filter(type=Agile.TYPE_VALUE)

    def get_principles(self) -> 'QuerySet[Agile]':
        return self.filter(type=Agile.TYPE_PRINCIPLE)


class Agile(models.Model):

    TYPE_VALUE = 'value'
    TYPE_PRINCIPLE = 'principle'
    AGILE_TYPES_CHOICES = (
        (TYPE_VALUE, 'Value'),
        (TYPE_PRINCIPLE, 'Principle'),
    )
    name = models.CharField(_('agile value/principle name'), max_length=100)
    description = models.TextField(
        _('agile description'),
        blank=True,
        default='',
        help_text='Description of the Agile Value or Principle.',
    )
    type =  models.CharField(
                max_length=20,
                choices=AGILE_TYPES_CHOICES,
                default=TYPE_VALUE
    )

    creation_date = models.DateTimeField(_('date created'), auto_now_add=True)
    modified_date = models.DateTimeField(
        _('date last modified'), auto_now=True
    )

    objects = AgileManager()

    class Meta:
        verbose_name_plural = _('Agile Values and Principles')

    def __str__(self) -> str:
        return f'{self.type}: {self.name}'
