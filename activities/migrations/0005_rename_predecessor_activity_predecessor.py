# Generated by Django 3.2.15 on 2022-11-12 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_activity_eventclass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='Predecessor',
            new_name='predecessor',
        ),
    ]
