# Generated by Django 3.2.23 on 2023-12-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_auto_20231228_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]