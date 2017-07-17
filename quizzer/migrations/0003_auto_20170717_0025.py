# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzer', '0002_auto_20170717_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsession',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
