from django.db import models

from django.utils.translation import gettext_lazy as _


class Continent(models.Model):
    is_published = models.BooleanField(('published'), default=True)
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('continent')
        verbose_name_plural = _('Continents')


class Country(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255
    )
    continent = models.ForeignKey(
        'Continent', related_name='country',
        verbose_name=_('continent'), on_delete=models.CASCADE,
    )
    flag = models.URLField(
        _('flag URLs'), null=True, max_length=255, blank=True
    )
    capital = models.CharField(_('capital'), max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('Country')
