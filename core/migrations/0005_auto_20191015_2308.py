# Generated by Django 2.2.4 on 2019-10-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191013_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashbord',
            name='single_player',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dashbord',
            name='team',
            field=models.CharField(max_length=20),
        ),
    ]
