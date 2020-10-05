# Generated by Django 2.2.14 on 2020-09-14 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20200828_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Continent', verbose_name='continent')),
            ],
            options={
                'verbose_name': 'Rating Associations',
            },
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=7, verbose_name='Points on association rating')),
                ('cl_teams', models.IntegerField(blank=True, default=0, verbose_name='The number of represented in the Champions League')),
                ('el_teams', models.IntegerField(blank=True, default=1, verbose_name='The number of represented in the Europe League')),
                ('country', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Country', verbose_name='Country')),
                ('rating', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.RatingAssociation', verbose_name='Rating Associations')),
            ],
            options={
                'verbose_name': 'Association',
            },
        ),
    ]