# Generated by Django 5.0.2 on 2024-02-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='main_pr_target',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='list',
            name='main_service',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='list',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='list',
            name='website_url',
            field=models.CharField(default='0000-0-0', max_length=10),
        ),
    ]