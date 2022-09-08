# Generated by Django 3.2.13 on 2022-09-08 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_category_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news.category', verbose_name='Категория'),
        ),
    ]
