# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzer', '0006_auto_20170717_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizsession',
            name='quiz',
        ),
        migrations.AddField(
            model_name='quizsession',
            name='quiz',
            field=models.ForeignKey(to='quizzer.Quiz', default=1),
            preserve_default=False,
        ),
    ]
