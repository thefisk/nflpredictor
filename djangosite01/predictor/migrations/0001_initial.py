# Generated by Django 2.1.7 on 2019-03-20 13:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Week', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(17)])),
                ('GameID', models.IntegerField(validators=[django.core.validators.MinValueValidator(2010010101)])),
                ('HomeScore', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('AwayScore', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('ShortName', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Town', models.CharField(max_length=20)),
                ('Nickname', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='results',
            name='AwayTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AwayTeam_Results_Set', to='predictor.Team'),
        ),
        migrations.AddField(
            model_name='results',
            name='HomeTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HomeTeam_Results_Set', to='predictor.Team'),
        ),
    ]
