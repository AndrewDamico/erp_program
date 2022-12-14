# Generated by Django 3.2.15 on 2022-11-12 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='sch_due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='sch_finish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='sch_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='finish_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_date',
            field=models.DateField(),
        ),
    ]
