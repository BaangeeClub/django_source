# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0009_auto_20150806_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('creation_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
