# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quizzer', '0005_quiz_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizsession',
            name='answers',
        ),
        migrations.AddField(
            model_name='quizsession',
            name='answers',
            field=picklefield.fields.PickledObjectField(default={None: None}, editable=False),
            preserve_default=False,
        ),
    ]
