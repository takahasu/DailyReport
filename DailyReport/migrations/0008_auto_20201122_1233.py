# Generated by Django 3.1.3 on 2020-11-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyReport', '0007_auto_20201122_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picking',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='搬出・ピッキング(h)※0.5h刻みで入力'),
        ),
    ]