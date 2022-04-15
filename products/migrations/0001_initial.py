# Generated by Django 3.2.6 on 2022-04-15 15:00

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='product_category', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория продуктов',
                'verbose_name_plural': 'Категории продуктов',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.IntegerField(max_length=6, unique=True, verbose_name='uuid')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='product', verbose_name='Фото')),
                ('qr', models.IntegerField(verbose_name='QR код')),
                ('description', models.CharField(blank=True, max_length=1024, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Средняя цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.productcategory')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
