# Generated by Django 3.2.15 on 2022-10-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0018_scopeitem_scopestatement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopeitem',
            name='fixed_cost',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='scopeitem',
            name='variable_cost',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
