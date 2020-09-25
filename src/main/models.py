import os

from django.db import models

from django.urls import reverse
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

class Continent(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255
    )
    image = models.ImageField(
        _('Image'), blank=True, null=True,
        upload_to='images/continent',
        help_text=_("Recomended size 512x512px")
    )
    main_text = models.TextField(_('main text'), null=True, blank=True)
    founded = models.DateTimeField(_('Founded'), default=timezone.now)
    located = models.CharField(
        _('Located'), null=True, max_length=255, blank=True
    )
    region = models.CharField(
        _('Region'), null=True, max_length=255, blank=True
    )
    associations = models.IntegerField(
        _('Count of associations'), default=1, blank=True
    )
    president = models.CharField(
        _('President'), null=True, max_length=255, blank=True
    )
    website = models.URLField(
        _('Website'), null=True, max_length=255, blank=True
    )
    is_published = models.BooleanField(('published'), default=True)
    published_at = models.DateTimeField(('published at'), default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('country_list', kwargs={'continent': self.slug})

    def get_absolute_club_rating_url(self):
        """Return category's URL"""
        return reverse('club-rating_page', kwargs={'continent': self.slug})

    def get_absolute_about_url(self):
        """Return category's URL"""
        return reverse('continent_about', kwargs={
            'continent': self.slug, 'pk': self.id
        })

    class Meta:
        verbose_name = ('continent')

class Country(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255
    )
    continent = models.ForeignKey(
        'Continent', related_name='country',
        verbose_name=_('continent'), on_delete=models.CASCADE,
    )
    main_text = models.TextField(_('main text'), null=True, blank=True)
    published_at = models.DateTimeField(('published at'), default=timezone.now)
    is_published = models.BooleanField(('published'), default=True)
    picture = models.ImageField(
        _('Image'), blank=True, null=True,
        upload_to='images/country',
        help_text=("Recomended size 512x512px")
    )
    flag = models.ImageField(
        _('Flag'), blank=True, null=True,
        upload_to='images/flag',
        help_text=("Recomended size 512x512px")
    )
    founded = models.DateTimeField(_('Founded'), default=timezone.now)
    fifa = models.DateField(
        _('Belonging to FIFA since'), default=timezone.now, blank=True
    )
    uefa = models.DateField(
        _('Belonging to since'), default=timezone.now, blank=True
    )
    president = models.CharField(
        _('President'), null=True, max_length=255, blank=True
    )
    website = models.URLField(
        _('Website'), null=True, max_length=255, blank=True
    )
    place = models.IntegerField(_('Place on rating'), default=1, blank=True)
    points = models.IntegerField(_('Points on rating'), default=1, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('league_list', kwargs={
            'continent': self.continent.slug, 'country': self.slug
        })

    def get_absolute_about_url(self):
        """Return category's URL"""
        return reverse('country_about', kwargs={
            'continent': self.continent.slug, 'country': self.slug,
            'pk': self.id
        })

    def get_cups(self):
        return CupCountry.objects.filter(
            country_id=self.pk
        ).order_by('-times', 'cup')

    def get_players(self):
        return CountryPlayer.objects.filter(
            country_id=self.pk
        ).order_by('player__title')

    class Meta:
        verbose_name = ('country')

class League(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255
    )
    picture = models.ImageField(
        _('Image'), blank=True, null=True,
        upload_to='images/league',
        help_text=_("Recomended size 512x512px")
    )
    main_text = models.TextField(_('main text'), null=True, blank=True)
    country = models.ForeignKey(
        'Country', related_name='league',
        verbose_name=_('country'), on_delete=models.CASCADE
    )
    founded = models.DateTimeField(_('Founded'), default=timezone.now)
    count_team = models.IntegerField(
        _('Number of teams:'), default=1, blank=True
    )
    reputation = models.IntegerField(
        _('Level on pyramid:'), default=1, blank=True
    )
    last = models.CharField(
        _('Last winner'), null=True, max_length=255, blank=True
    )
    website = models.URLField(
        _('Website'), null=True, max_length=255, blank=True
    )
    published_at = models.DateTimeField(('published at'), default=timezone.now)
    is_published = models.BooleanField(('published'), default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('club_list', kwargs={
            'continent': self.country.continent.slug,
            'country': self.country.slug, 'league': self.slug
        })

    def get_absolute_about_url(self):
        """Return category's URL"""
        return reverse('league_about', kwargs={
            'continent': self.country.continent.slug,
            'country': self.country.slug, 'league': self.slug, 'pk': self.id
        })

    class Meta:
        verbose_name = ('league')

class Cup(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255, null=True
    )
    image = models.ImageField(
        _('Image'), blank=True, null=True,
        upload_to='images/cup',
        help_text=_("Recomended size 512x512px")
    )
    main_text = models.TextField(_('main text'), null=True, blank=True)
    founded = models.DateTimeField(_('Founded'), default=timezone.now)
    region = models.ForeignKey(
        'Continent', related_name='cup',
        verbose_name=_('continent'),
        on_delete=models.CASCADE, null=True, blank=True
    )
    website = models.URLField(
        _('Website'), null=True, max_length=255, blank=True
    )

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('cup_detail', kwargs={'cup': self.slug, 'pk': self.id})

    def __str__(self):
        return self.title

    def get_players(self):
        return PlayerCup.objects.filter(
            cup_id=self.pk
        ).order_by('-times', 'player')

    def get_clubs(self):
        return CupClub.objects.filter(
            cup_id=self.pk
        ).order_by('-times', 'club')

    def get_countries(self):
        return CupCountry.objects.filter(
            cup_id=self.pk
        ).order_by('-times', 'country')

    class Meta:
        verbose_name = ('cup')

class Player(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255, null=True
    )
    image = models.ImageField(
        _('Image'), blank=True, null=True,
        upload_to='images/player',
        help_text=_("Recomended size 512x512px")
    )
    main_text = models.TextField(_('main text'), null=True, blank=True)
    country = models.ForeignKey(
        'Country', related_name='player',
        verbose_name=_('country'), on_delete=models.CASCADE, null=True
    )
    nickname = models.CharField(
        _('nickname'), null=True, max_length=255, blank=True
    )
    date_of_birth = models.DateTimeField(
        _('date of birth'), default=timezone.now
    )
    height = models.FloatField(_('height'), null=True, blank=True)
    positions = models.CharField(
        _('positions'), max_length=50, null=True, blank=True
    )

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('player_detail', kwargs={
            'player': self.slug, 'pk': self.id
        })

    def __str__(self):
        return self.title

    def get_fifa(self):
        return Fifa.objects.filter(player_id=self.pk)

    def get_clubs(self):
        return PlayerClub.objects.filter(
            player_id=self.pk
        ).order_by('year_from', '-year_to')

    def get_cups(self):
        return PlayerCup.objects.filter(
            player_id=self.pk
        ).order_by('-times', 'cup')

    class Meta:
        verbose_name = _('player')

class Club(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(
        _('slug'), unique=True, max_length=255
    )
    continent = models.ForeignKey(
        'Continent', null=True, related_name='club',
        verbose_name=_('continent'), on_delete=models.CASCADE,
    )
    league = models.ForeignKey(
        'League', related_name='club',
        verbose_name=_('league'), on_delete=models.CASCADE,
    )
    main_text = models.TextField(
        _('main text'), null=True, blank=True
    )
    published_at = models.DateTimeField(
        _('published at'), default=timezone.now)
    is_published = models.BooleanField(_('published'), default=True)
    picture = models.ImageField(
        _('Club emblem'), blank=True, null=True,
        upload_to='images/club',
        help_text=_("Recomended size 512x512px")
    )
    color1 = models.CharField(
        _('Color 1'), max_length=20, null=False, blank=True
    )
    color2 = models.CharField(
        _('Color 2'), max_length=20, null=False, blank=True
    )
    nickname = models.CharField(
        _('Nickname'), null=True, max_length=255, blank=True
    )
    short_name = models.CharField(
        _('Short name'), null=True, max_length=255, blank=True
    )
    founded = models.DateTimeField(
        _('Founded'), default=timezone.now
    )
    stadium = models.CharField(
        _('Stadium'), null=True, max_length=255, blank=True
    )
    manager = models.CharField(
        _('Manager'), null=True, max_length=255, blank=True
    )
    website = models.URLField(
        _('Website'), null=True, max_length=255, blank=True
    )
    place = models.IntegerField(
        _('Place on rating'), default=1, blank=True
    )
    points = models.DecimalField(
        _('Points on rating'), max_digits=7, decimal_places=3,
        default=1, blank=True
    )

    class Meta:
        verbose_name = _("Club")

    def __str__(self):
        return self.title

    def get_kits(self):
        return Kits.objects.filter(club_id=self.pk)

    def get_player(self):
        return PlayerClub.objects.filter(
            club_id=self.pk
        ).order_by('player__title')

    def get_cups(self):
        return CupClub.objects.filter(
            club_id=self.pk
        ).order_by('-times', 'cup__title')

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('club_detail', kwargs={
            'continent': self.league.country.continent.slug,
            'country': self.league.country.slug,
            'league': self.league.slug,
            'club': self.slug, 'pk': self.id
        })

class Kits(models.Model):
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, verbose_name=("Club")
    )
    title = models.CharField(max_length=200, default='Kits')
    kits = models.ImageField(
        ("Kits"), upload_to="images/kits", null=True, blank=True
    )

    def get_extension(self):
        file_extension = os.path.splitext(self.kits.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.kits.name)

    class Meta:
        verbose_name = _("Kit")

class Fifa(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, verbose_name=("Player")
    )
    cards = models.ImageField(
        ("Fifa"), upload_to="images/fifa", null=True, blank=True
    )

    def get_extension(self):
        file_extension = os.path.splitext(self.fifa.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.fifa.name)

    class Meta:
        verbose_name = _("Fifa")


class PlayerClub(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, verbose_name=("Player")
    )
    club = models.ForeignKey(
        'Club', related_name='player',
        verbose_name=_('club'), on_delete=models.CASCADE,
    )
    year_from = models.PositiveIntegerField(
        verbose_name=_('Year from'), blank=True
    )
    year_to = models.PositiveIntegerField(
        verbose_name=_('Year to'), blank=True
    )
    games = models.PositiveIntegerField(
        verbose_name=_('Games'), blank=True, default=0
    )
    score = models.IntegerField(
        verbose_name=_('Score'), blank=True, default=0
    )
    is_load = models.BooleanField(('Load'), default=False)
    years_in_club = models.TextField(
        _('Year in club'), null=True, blank=True
    )
    first_time = models.BooleanField(('First time?'), default=True)

    def get_extension(self):
        file_extension = os.path.splitext(self.playerclub.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.playerclub.name)

    class Meta:
        verbose_name = _("Player Club")

class PlayerCup(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, verbose_name=_("Player")
    )
    cup = models.ForeignKey(
        Cup, verbose_name=_('Cup'), on_delete=models.CASCADE, default=None
    )
    times = models.PositiveIntegerField(
        verbose_name=_('Now much?'), blank=True
    )
    years = models.TextField(
        _('Years'), null=True, blank=True
    )

    def get_extension(self):
        file_extension = os.path.splitext(self.playercup.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.playercup.name)

    class Meta:
        verbose_name = _("Player Cup")

class CupClub(models.Model):
    cup = models.ForeignKey(
        Cup, verbose_name=_('Cup'), on_delete=models.CASCADE, default=None
    )
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, verbose_name=("Club")
    )
    times = models.PositiveIntegerField(
        verbose_name=_('Now much?'), blank=True
    )

    def get_extension(self):
        file_extension = os.path.splitext(self.cupclub.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.cupclub.name)

    class Meta:
        verbose_name = _("Cup Club")

class CupCountry(models.Model):
    cup = models.ForeignKey(
        Cup, verbose_name=_('Cup'), on_delete=models.CASCADE, default=None
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=("Country")
    )
    times = models.PositiveIntegerField(
        verbose_name=_('Now much?'), blank=True
    )

    def get_extension(self):
        file_extension = os.path.splitext(self.cupcountry.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.cupcountry.name)

    class Meta:
        verbose_name = _("Cup Country")

class CountryPlayer(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, verbose_name=_("Player")
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=("Country"),
        default=None
    )
    year_from = models.PositiveIntegerField(
        verbose_name=_('Year from'), blank=True
    )
    year_to = models.PositiveIntegerField(
        verbose_name=_('Year to'), blank=True
    )
    one_time = models.BooleanField(('One time?'), default=True)
    years = models.TextField(
        _('Years'), null=True, blank=True
    )

    def get_extension(self):
        file_extension = os.path.splitext(self.countryplayer.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.countryplayer.name)

    class Meta:
        verbose_name = _("Cup Country")


class RatingAssociation(models.Model):
    continent = models.ForeignKey(
        'Continent', null=True,
        verbose_name=_('continent'), on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('association-rating_page', kwargs={
            'ratingass': self.continent.slug, 'pk': self.id
        })

    def __str__(self):
        return self.continent.title

    class Meta:
        verbose_name = _('Rating Associations')

    def get_ass(self):
        return Association.objects.filter(
            rating_id=self.pk
        ).order_by('points')


class Association(models.Model):
    rating = models.ForeignKey(
        RatingAssociation, on_delete=models.CASCADE, verbose_name=("Rating Associations"),
        default=None
    )
    place = models.IntegerField(
        _('Place'), blank=True, default=1
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=("Country"),
        default=None
    )
    point_year1 = models.DecimalField(
        _('Points on association rating'), max_digits=7,
        decimal_places=3, default=1, blank=True
    )
    point_year2 = models.DecimalField(
        _('Points on association rating'), max_digits=7,
        decimal_places=3, default=1, blank=True
    )
    point_year3 = models.DecimalField(
        _('Points on association rating'), max_digits=7,
        decimal_places=3, default=1, blank=True
    )
    point_year4 = models.DecimalField(
        _('Points on association rating'), max_digits=7,
        decimal_places=3, default=1, blank=True
    )
    point_year5 = models.DecimalField(
        _('Points on association rating'), max_digits=7,
        decimal_places=3, default=1, blank=True
    )
    points = models.DecimalField(
        _('Points on association rating'), max_digits=7,
        decimal_places=3, default=1, blank=True
    )
    teams = models.IntegerField(
        _('The number of represented Euro Cups'),
        default=0, blank=True
    )

    def get_extension(self):
        file_extension = os.path.splitext(self.association.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.association.name)

    class Meta:
        verbose_name = _("Association")
