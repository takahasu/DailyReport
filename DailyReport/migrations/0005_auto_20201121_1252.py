# Generated by Django 3.1.3 on 2020-11-21 12:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0004_auto_20201121_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picking',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric are allowed.')], verbose_name='搬出・ピッキング'),
        ),
        migrations.AlterField(
            model_name='item',
            name='takuhaikaikon',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric are allowed.')], verbose_name='宅配開梱'),
        ),
    ]
