# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0002_auto_20150122_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='closet',
            old_name='owner',
            new_name='user',
        ),
    ]
