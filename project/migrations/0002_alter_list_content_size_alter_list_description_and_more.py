# Generated by Django 5.0.2 on 2024-02-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='content_size',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='list',
            name='recruitment_number',
            field=models.IntegerField(default=0),
        ),
    ]
