# Generated by Django 2.0.5 on 2018-07-31 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_request', '0003_auto_20180706_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 31, 18, 36, 46, 728564)),
            preserve_default=False,
        ),
    ]
