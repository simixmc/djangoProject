# Generated by Django 3.2.13 on 2022-09-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_mainmenu_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmenu',
            name='sort',
            field=models.IntegerField(max_length=15, null=True, verbose_name='Сортировка'),
        ),
    ]
