# Generated by Django 2.1.7 on 2019-06-10 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0018_auto_20190610_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='Banker',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='Week',
        ),
    ]