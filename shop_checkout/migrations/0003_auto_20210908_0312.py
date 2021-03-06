# Generated by Django 3.2.6 on 2021-09-08 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_item_sku'),
        ('shop_checkout', '0002_auto_20210904_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unitorder',
            name='unit',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='billing_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unitorder',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_units', to='shop.item'),
        ),
        migrations.AlterField(
            model_name='unitorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='shop_checkout.orderdetails'),
        ),
        migrations.AlterField(
            model_name='unitorder',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
