# Generated by Django 3.2.15 on 2022-10-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0016_auto_20221022_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='schedule_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
