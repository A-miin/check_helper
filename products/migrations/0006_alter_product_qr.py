# Generated by Django 3.2.6 on 2022-05-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220505_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qr',
            field=models.IntegerField(blank=True, null=True, verbose_name='QR код'),
        ),
    ]
