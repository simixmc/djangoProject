# Generated by Django 3.2.13 on 2022-09-09 14:09

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220909_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.category', verbose_name='Категория'),
        ),
    ]
