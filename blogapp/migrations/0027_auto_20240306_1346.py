# Generated by Django 3.2.24 on 2024-03-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0026_auto_20240301_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
