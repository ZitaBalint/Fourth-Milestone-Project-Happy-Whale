# Generated by Django 3.2.6 on 2021-09-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_checkout', '0004_auto_20210908_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='order_number',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='order_key',
            field=models.CharField(default=1, editable=False, max_length=200),
        ),
    ]
