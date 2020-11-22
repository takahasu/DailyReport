# Generated by Django 3.1.3 on 2020-11-21 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0005_auto_20201121_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cleaning',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)], verbose_name='クリーニング'),
        ),
        migrations.AlterField(
            model_name='item',
            name='dataerase',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='データイレース'),
        ),
        migrations.AlterField(
            model_name='item',
            name='shiiresyouhinka',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5000)], verbose_name='仕入商品化'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tsutaya',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)], verbose_name='TSUTAYA関連'),
        ),
    ]