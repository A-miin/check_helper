# Generated by Django 3.2.6 on 2022-04-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220415_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.CharField(blank=True, max_length=64, unique=True, verbose_name='uuid'),
        ),
    ]
