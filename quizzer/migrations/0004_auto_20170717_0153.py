# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzer', '0003_auto_20170717_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizsession',
            old_name='end',
            new_name='date_taken',
        ),
        migrations.RemoveField(
            model_name='quizsession',
            name='start',
        ),
    ]
