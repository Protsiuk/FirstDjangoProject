# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20170506_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicationcomment',
            old_name='text_comment',
            new_name='text',
        ),
    ]
