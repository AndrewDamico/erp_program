# Generated by Django 3.2.15 on 2022-11-12 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a2dam', '0001_initial'),
        ('activities', '0003_activity_sch_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='eventclass',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='a2dam.eventclass'),
            preserve_default=False,
        ),
    ]
