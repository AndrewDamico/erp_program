# Generated by Django 3.2.15 on 2022-10-21 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0008_quarter'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseinfo',
            name='quarter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='budget_app.quarter'),
            preserve_default=False,
        ),
    ]
