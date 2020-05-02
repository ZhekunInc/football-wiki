from django.db import models

from django.urls import reverse
from django.utils import timezone

class Continent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        ('slug'), unique=True, max_length=255,
        help_text=("Used to build the category's URL.")
    )
    is_published = models.BooleanField(('published'), default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('country_list', kwargs={'continent': self.slug})
    
    class Meta:
        verbose_name = ('continent')

class Country(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        ('slug'), unique=True, max_length=255,
        help_text=("Used to build the category's URL.")
    )
    continent = models.ForeignKey(
        'Continent', related_name='country',
        verbose_name=('continent'), on_delete=models.CASCADE,
    )
    published_at = models.DateTimeField(('published at'), default=timezone.now)
    is_published = models.BooleanField(('published'), default=True)
    picture = models.ImageField(
        'Image', blank=True, null=True,
        upload_to='images/country',
        help_text=("Recomended size 512x512px")
    )
    wc = models.IntegerField(default=1)
    cl = models.IntegerField(default=1)
    gb = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('league_list', kwargs={'continent': self.continent.slug, 'country': self.slug})

    class Meta:
        verbose_name = ('country')

class League(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        ('slug'), unique=True, max_length=255,
        help_text=("Used to build the category's URL.")
    )
    country = models.ForeignKey(
        'Country', related_name='league',
        verbose_name=('country'), on_delete=models.CASCADE
    )
    reputation = models.IntegerField(default=1)
    published_at = models.DateTimeField(('published at'), default=timezone.now)
    is_published = models.BooleanField(('published'), default=True)
    picture = models.ImageField(
        'Image', blank=True, null=True,
        upload_to='images/league',
        help_text=("Recomended size 512x512px")
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('club_list', kwargs={'continent': self.country.continent.slug, 'country': self.country.slug, 'league': self.slug})

    class Meta:
        verbose_name = ('league')

class Cup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        ('slug'), unique=True, max_length=255,
        help_text=("Used to build the category's URL."), null=True
    )
    image = models.ImageField(
        'Image', blank=True, null=True,
        upload_to='images/cup',
        help_text=("Recomended size 512x512px")
    )
    main_text = models.TextField(null=True)
    players = models.ManyToManyField(
        'Player', related_name='cup',
        verbose_name=('player'), blank=True
    )
    clubs = models.ManyToManyField(
        'Club', related_name='cup',
        verbose_name=('club'), blank=True
    )
    countrys = models.ManyToManyField(
        'Country', related_name='cup',
        verbose_name=('country'), blank=True
    )
    founded = models.DateTimeField(default=timezone.now)
    region = models.ForeignKey(
        'Continent', related_name='cup',
        verbose_name=('continent'), on_delete=models.CASCADE, null=True
    )
    website = models.URLField(null=True, max_length=255)

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('cup_detail', kwargs={'cup': self.slug, 'pk': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('cup')
    
class Player(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        ('slug'), unique=True, max_length=255,
        help_text=("Used to build the category's URL."), null=True
    )
    image = models.ImageField(
        'Image', blank=True, null=True,
        upload_to='images/player',
        help_text=("Recomended size 512x512px")
    )
    main_text = models.TextField(null=True)
    country = models.ForeignKey(
        'Country', related_name='player',
        verbose_name=('country'), on_delete=models.CASCADE, null=True
    )
    clubs = models.ManyToManyField(
        'Club', related_name='player',
        verbose_name=('club'), blank=True
    )
    cups = models.ManyToManyField(
        'Cup', related_name='player',
        verbose_name=('cup'), blank=True
    )
    nickname = models.CharField(null=True, max_length=255)
    date_of_birth = models.DateTimeField(default=timezone.now)
    height = models.FloatField(null=True)
    positions = models.CharField(max_length=50, null=True)
    wc = models.IntegerField(default=1)
    cl = models.IntegerField(default=1)
    gb = models.IntegerField(default=1)
    
    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('player_detail', kwargs={'player': self.slug, 'pk': self.id})

    def __str__(self):
        return self.title

    def get_fifa(self):
        return Fifa.objects.filter(player_id=self.pk)

    class Meta:
        verbose_name = ('player')

class Club(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        ('slug'), unique=True, max_length=255,
        help_text=("Used to build the category's URL.")
    )
    league = models.ForeignKey(
        'League', related_name='club',
        verbose_name=('league'), on_delete=models.CASCADE,
    )
    main_text = models.TextField(null=True)
    published_at = models.DateTimeField(('published at'), default=timezone.now)
    is_published = models.BooleanField(('published'), default=True)
    picture = models.ImageField(
        'Image', blank=True, null=True,
        upload_to='images/club',
        help_text=("Recomended size 512x512px")
    )
    nickname = models.CharField(null=True, max_length=255)
    short_name = models.CharField(null=True, max_length=255)
    founded = models.DateTimeField(default=timezone.now)
    stadium = models.CharField(null=True, max_length=255)
    manager = models.CharField(null=True, max_length=255)
    website = models.URLField(null=True, max_length=255)
    cups = models.ManyToManyField(
        'Cup', related_name='club',
        verbose_name=('cup'), blank=True
    )
    famous_players = models.ManyToManyField(
        'Player', related_name='club',
        verbose_name=('player'), blank=True
    )
    cl = models.IntegerField(default=0)
    gb = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("Club")
    
    def __str__(self):
        return self.title

    def get_kits(self):
        return Kits.objects.filter(club_id=self.pk)

    def get_absolute_url(self):
        """Return category's URL"""
        return reverse('club_detail', kwargs={'continent': self.league.country.continent.slug,
         'country': self.league.country.slug, 'league': self.league.slug, 'club': self.slug, 'pk': self.id})

class Kits(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name=("Club"))
    title = models.CharField(max_length=200, default='Kits')
    kits = models.ImageField(("Kits"), upload_to="images/kits", null=True, blank=True)

    def get_extension(self):
        file_extension=os.path.splitext(self.kits.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.kits.name)

    class Meta: 
        verbose_name = ("Kit")

class Fifa(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name=("Player"))
    cards = models.ImageField(("Fifa"), upload_to="images/fifa", null=True, blank=True)

    def get_extension(self):
        file_extension=os.path.splitext(self.fifa.path)
        return file_extension[1]

    def get_filename(self):
        return os.path.basename(self.fifa.name)

    class Meta: 
        verbose_name = ("Fifa")
