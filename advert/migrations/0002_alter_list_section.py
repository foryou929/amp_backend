# Generated by Django 5.0.3 on 2024-03-08 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
        ('section', '0002_alter_list_project_alter_list_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advert_section', to='section.list'),
        ),
    ]
