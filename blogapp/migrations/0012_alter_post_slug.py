# Generated by Django 3.2.23 on 2023-12-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_auto_20231228_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
