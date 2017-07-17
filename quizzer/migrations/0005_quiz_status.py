# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzer', '0004_auto_20170717_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='status',
            field=models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft'),
        ),
    ]
