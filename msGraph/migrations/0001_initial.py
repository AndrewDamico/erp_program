# Generated by Django 3.2.15 on 2022-11-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutlookEvent',
            fields=[
                ('subject', models.CharField(max_length=512)),
                ('body', models.TextField(blank=True, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('change_key', models.CharField(max_length=128)),
                ('organizer', models.CharField(max_length=128)),
                ('show_as', models.CharField(max_length=16)),
            ],
        ),
    ]
