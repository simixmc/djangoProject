# Generated by Django 3.2.13 on 2022-09-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_topbar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='path',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='URL'),
        ),
    ]
