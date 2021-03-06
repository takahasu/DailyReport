# Generated by Django 3.1.3 on 2020-11-19 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('高橋悠人', '高橋悠人'), ('足立雄介', '足立雄介'), ('井上貴子', '井上貴子'), ('柿崎義弘', '柿崎義弘'), ('斎藤祐樹', '斎藤祐樹'), ('和田昭雄', '和田昭雄')], max_length=20, verbose_name='名前')),
                ('takuhaikenpin', models.IntegerField(default=0, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric are allowed.')], verbose_name='宅配検品')),
                ('sonotakenpin', models.IntegerField(default=0, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric are allowed.')], verbose_name='その他検品')),
                ('sex', models.IntegerField(choices=[(1, '男性'), (2, '女性'), (3, 'テスト')], default=1, verbose_name='性別')),
                ('memo', models.TextField(blank=True, max_length=300, null=True, verbose_name='備考')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
            ],
            options={
                'verbose_name': 'アイテム',
                'verbose_name_plural': 'アイテム',
            },
        ),
    ]
