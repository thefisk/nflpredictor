# Generated by Django 2.1.7 on 2019-08-15 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0026_auto_20190815_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoresalltime',
            name='User',
        ),
        migrations.DeleteModel(
            name='ScoresAllTime',
        ),
    ]