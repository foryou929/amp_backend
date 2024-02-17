# Generated by Django 5.0.2 on 2024-02-17 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('birthday', models.DateTimeField()),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Undefined'), (1, 'Type A'), (2, 'Type B'), (3, 'Type C'), (4, 'Other')], default=0)),
                ('gendor', models.PositiveSmallIntegerField(choices=[(0, 'Undefined'), (1, 'Male'), (2, 'Female'), (3, 'Other')], default=0)),
                ('occupation', models.PositiveSmallIntegerField(choices=[(0, 'Undefined'), (1, 'Student'), (2, 'Professional'), (3, 'Unemployed'), (4, 'Other')], default=0)),
                ('primary_transportation', models.PositiveSmallIntegerField(choices=[(0, 'Undefined'), (1, 'Car'), (2, 'Bicycle'), (3, 'Public transportation'), (4, 'Walking'), (5, 'Other')], default=0)),
                ('residence_type', models.PositiveSmallIntegerField(choices=[(0, 'Undefined'), (1, 'House'), (2, 'Apartment'), (3, 'Condo'), (4, 'Other')], default=0)),
                ('self_introduction', models.TextField(default='')),
                ('activity_scope', models.CharField(default='', max_length=100)),
                ('area', models.PositiveIntegerField(default=0)),
                ('available_space', models.PositiveIntegerField(default=0)),
                ('follower_count', models.PositiveIntegerField(default=0)),
                ('usage_frequency', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
