# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-14 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipanaro', '0008_delete_membershiplevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='nid_type',
            field=models.IntegerField(choices=[(7240, 'Passport'), (7241, 'Documento Nacional de Identidad'), (7242, 'Número de Identificación de Extranjeros'), (0, 'Unknown')]),
        ),
    ]
