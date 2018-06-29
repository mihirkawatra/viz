# Generated by Django 2.0.5 on 2018-06-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_url', models.URLField(max_length=30)),
                ('vid_url', models.URLField(max_length=30, unique=True)),
            ],
        ),
    ]
