# Generated by Django 2.2.4 on 2019-10-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashbord',
            name='single_player',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='dashbord',
            name='team',
            field=models.CharField(default='', max_length=20),
        ),
    ]
