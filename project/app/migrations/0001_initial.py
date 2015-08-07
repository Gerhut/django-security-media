# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public', models.FileField(upload_to=b'')),
                ('private', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/security_media/', location=b'C:\\Users\\gerhut\\django-security-media\\project\\security_media'), upload_to=b'')),
            ],
            options={
                'verbose_name': 'Key',
                'verbose_name_plural': 'Keys',
            },
            bases=(models.Model,),
        ),
    ]
