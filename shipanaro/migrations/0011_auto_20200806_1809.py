# Generated by Django 3.1 on 2020-08-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipanaro', '0010_auto_20200805_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='nid_type',
            field=models.IntegerField(choices=[(7240, 'Passport'), (7241, 'Documento Nacional de Identidad'), (7242, 'Número de Identificación de Extranjeros'), (0, 'Desconegut')]),
        ),
    ]