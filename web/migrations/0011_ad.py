# Generated by Django 4.1.3 on 2022-11-16 05:52

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_image', versatileimagefield.fields.VersatileImageField(upload_to='image/testimagemodel/', verbose_name='Image')),
                ('ad_product_name', models.CharField(max_length=100)),
                ('ad_title', models.CharField(max_length=100)),
                ('offer_title', models.CharField(max_length=100)),
            ],
        ),
    ]