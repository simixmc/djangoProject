# Generated by Django 3.2.13 on 2022-09-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='path',
            field=models.CharField(max_length=500, null=True, verbose_name='URL'),
        ),
    ]
