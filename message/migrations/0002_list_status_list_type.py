# Generated by Django 5.0.2 on 2024-02-23 16:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
