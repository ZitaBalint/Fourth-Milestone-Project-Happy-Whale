# Generated by Django 3.2.6 on 2021-08-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210816_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_code',
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
