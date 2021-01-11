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
    flag_file = models.ImageField(
        _('Flag'), max_length=255, blank=True, null=True,
        upload_to='images/geo/flags',
        help_text=_("Recomended size 512x512px")
    )
    capital = models.CharField(_('capital'), max_length=200)

    def __str__(self):
        return self.title

    def get_download_url_or_none(self):
        if self.flag and "drive.google.com" in self.flag:
            if self.flag.endswith('download'):
                return self.flag

            flag = self.flag.replace("https://drive.google.com/file/d/", "")
            flag = flag.replace("https://drive.google.com/open?id=", "")
            img_id = flag[:33]
            flag = "https://docs.google.com/uc?id=%s" % img_id
            return flag
        if self.flag:
            return self.flag
        return None

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('Country')
