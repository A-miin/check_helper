# Generated by Django 3.2.6 on 2022-04-21 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disease_recommendations', '0003_recommendation_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to=settings.AUTH_USER_MODEL),
        ),
    ]
