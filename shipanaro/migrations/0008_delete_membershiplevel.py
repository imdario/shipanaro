# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-28 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipanaro', '0007_membershiplevel'),
    ]

    operations = [
        migrations.DeleteModel(name='MembershipLevel', ),
    ]
