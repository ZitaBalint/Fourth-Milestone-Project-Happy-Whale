# Generated by Django 3.2.6 on 2021-08-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_category_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
