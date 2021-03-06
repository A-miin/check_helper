# Generated by Django 3.2.6 on 2022-04-15 15:57

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qr',
            field=models.IntegerField(blank=True, verbose_name='QR код'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='uuid'),
        ),
    ]
