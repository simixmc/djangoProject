# Generated by Django 3.2.13 on 2022-09-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220913_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='sort',
            field=models.IntegerField(default=100, verbose_name='Сортировка'),
        ),
    ]
