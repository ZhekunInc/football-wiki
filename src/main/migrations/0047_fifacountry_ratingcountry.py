# Generated by Django 2.2.14 on 2020-10-15 15:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20201015_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='published at')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Continent', verbose_name='continent')),
            ],
            options={
                'verbose_name': 'Rating Teams',
            },
        ),
        migrations.CreateModel(
            name='FifaCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(blank=True, default=1, verbose_name='Place')),
                ('points', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='Points on association rating')),
                ('place_continent', models.IntegerField(blank=True, default=1, verbose_name='Place in continent')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Continent', verbose_name='continent')),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Country', verbose_name='Club')),
                ('rating', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.RatingCountry', verbose_name='Rating Continent')),
            ],
            options={
                'verbose_name': 'FifaCountry',
            },
        ),
    ]
