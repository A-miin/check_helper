# Generated by Django 3.2.6 on 2022-05-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Средняя цена'),
        ),
    ]