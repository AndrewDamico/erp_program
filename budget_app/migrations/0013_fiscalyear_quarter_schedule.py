# Generated by Django 3.2.15 on 2022-10-22 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0012_delete_navbar_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiscalYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FY_name', models.CharField(max_length=20)),
                ('FY_start_date', models.DateTimeField(verbose_name='FY Start Date')),
                ('FY_end_date', models.DateTimeField(verbose_name='FY End Date')),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Schedule Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Schedule End Date')),
                ('fiscalyear', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='budget_app.fiscalyear')),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='budget_app.quarter')),
            ],
        ),
    ]
