# Generated by Django 5.0.2 on 2024-02-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='step',
            field=models.IntegerField(default=0),
        ),
    ]
