# Generated by Django 4.0.3 on 2022-03-17 00:26

import apps.profiles.models
from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cell_phone',
            field=models.CharField(blank=True, default='', max_length=25, null=True, verbose_name='Telefone Celular'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=localflavor.br.models.BRPostalCodeField(blank=True, default='', max_length=9, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=localflavor.br.models.BRStateField(blank=True, default='', max_length=2, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='profile_default.png', upload_to=apps.profiles.models.upload_perfil_user, verbose_name='Profile Photo'),
        ),
    ]
