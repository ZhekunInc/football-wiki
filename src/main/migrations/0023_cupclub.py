# Generated by Django 2.2.14 on 2020-08-28 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200819_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.PositiveIntegerField(blank=True, verbose_name='Now much?')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Club', verbose_name='Club')),
            ],
            options={
                'verbose_name': 'Cup Club',
            },
        ),
    ]