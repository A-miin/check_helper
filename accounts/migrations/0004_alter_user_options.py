# Generated by Django 3.2.6 on 2022-04-15 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220413_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('is_activated',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
