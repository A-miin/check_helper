# Generated by Django 3.2.6 on 2022-04-21 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_disease'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='disease',
            new_name='diseases',
        ),
    ]
