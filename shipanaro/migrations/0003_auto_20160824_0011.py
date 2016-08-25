# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [('shipanaro', '0002_auto_20160815_2344'), ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='to_field', ),
        migrations.AddField(
            model_name='membership',
            name='contact_id',
            field=models.CharField(
                default='', max_length=9),
            preserve_default=False, ),
        migrations.AddField(
            model_name='membership',
            name='date_left',
            field=models.DateField(null=True), ),
        migrations.AddField(
            model_name='membership',
            name='notes',
            field=models.TextField(blank=True), ),
        migrations.AddField(
            model_name='membership',
            name='phone_2',
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128), ),
        migrations.AddField(
            model_name='membership',
            name='province',
            field=models.CharField(
                default='', max_length=70),
            preserve_default=False, ),
        migrations.AddField(
            model_name='subscription',
            name='endpoint',
            field=models.TextField(default=''),
            preserve_default=False, ),
        migrations.AlterField(
            model_name='membership',
            name='address',
            field=models.CharField(max_length=140), ),
        migrations.AlterField(
            model_name='membership',
            name='assigned_sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (
                9, 'Not Applicable')]), ),
        migrations.AlterField(
            model_name='membership',
            name='birthday',
            field=models.DateField(), ),
        migrations.AlterField(
            model_name='membership',
            name='city',
            field=models.CharField(max_length=70), ),
        migrations.AlterField(
            model_name='membership',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (
                9, 'Gender non-conforming')]), ),
        migrations.AlterField(
            model_name='membership',
            name='nationality',
            field=models.CharField(max_length=20), ),
        migrations.AlterField(
            model_name='membership',
            name='nid',
            field=models.CharField(max_length=50), ),
        migrations.AlterField(
            model_name='membership',
            name='nid_type',
            field=models.IntegerField(choices=[
                (7240, 'Passport'), (7241, 'Documento Nacional de Identidad'),
                (7242, 'Número de Identificación de Extranjeros'),
                (0, 'Unknown')
            ]), ),
        migrations.AlterField(
            model_name='membership',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128), ),
        migrations.AlterField(
            model_name='membership',
            name='postal_code',
            field=models.CharField(max_length=20), ),
    ]
