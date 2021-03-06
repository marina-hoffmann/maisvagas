# Generated by Django 4.0.5 on 2022-06-09 23:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data_criacao', models.DateField(blank=True, default=datetime.datetime.now)),
                ('local', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('requisitos', models.TextField()),
                ('beneficios', models.TextField()),
                ('publicada', models.BooleanField(default=False)),
                ('categoria', models.CharField(max_length=50)),
                ('senioridade', models.CharField(max_length=10)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
