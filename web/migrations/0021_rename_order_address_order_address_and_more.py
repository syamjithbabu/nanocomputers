# Generated by Django 4.1.3 on 2022-11-21 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_order_pin_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pin_code',
            new_name='pincode',
        ),
    ]
