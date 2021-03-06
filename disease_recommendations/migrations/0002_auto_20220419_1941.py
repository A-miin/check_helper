# Generated by Django 3.2.6 on 2022-04-19 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease_recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DiseaseCategory',
            new_name='DiseaseTag',
        ),
        migrations.AlterModelOptions(
            name='diseasetag',
            options={'verbose_name': 'Тэг болезней', 'verbose_name_plural': 'Тэги болезней'},
        ),
        migrations.RemoveField(
            model_name='disease',
            name='category',
        ),
        migrations.AddField(
            model_name='disease',
            name='tags',
            field=models.ManyToManyField(related_name='diseases', to='disease_recommendations.DiseaseTag'),
        ),
    ]
