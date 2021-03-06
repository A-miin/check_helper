# Generated by Django 3.2.6 on 2022-04-15 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Болезнь',
                'verbose_name_plural': 'Болезни',
            },
        ),
        migrations.CreateModel(
            name='DiseaseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=1024, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория болезней',
                'verbose_name_plural': 'Категории болезней',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(default=0, verbose_name='Процент противопоказаний')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='disease_recommendations.disease')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='products.product')),
            ],
            options={
                'verbose_name': 'Рекомендация',
                'verbose_name_plural': 'Рекомендации',
            },
        ),
        migrations.AddField(
            model_name='disease',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diseases', to='disease_recommendations.diseasecategory'),
        ),
    ]
