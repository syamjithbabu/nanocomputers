# Generated by Django 4.1.3 on 2022-11-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pin_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
