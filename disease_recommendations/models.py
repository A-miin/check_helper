from django.db import models
from django.utils.translation import gettext_lazy as _


class DiseaseTag(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=128,
    )
    description = models.CharField(
        verbose_name=_('Описание'),
        max_length=1024,
        blank=True
    )

    class Meta:
        verbose_name = _('Тэг болезней')
        verbose_name_plural = _('Тэги болезней')

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=128,
    )
    description = models.CharField(
        verbose_name=_('Описание'),
        max_length=1024,
        blank=True,
    )
    tags = models.ManyToManyField(
        'disease_recommendations.DiseaseTag',
        related_name='diseases',
    )

    class Meta:
        verbose_name = _('Болезнь')
        verbose_name_plural = _('Болезни')

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='recommendations',
    )
    disease = models.ForeignKey(
        'disease_recommendations.Disease',
        on_delete=models.CASCADE,
        related_name='recommendations',
    )
    percent = models.FloatField(
        verbose_name=_('Процент противопоказаний'),
        default=0,
    )

    class Meta:
        verbose_name = _('Рекомендация')
        verbose_name_plural = _('Рекомендации')

    def __str__(self):
        return f'{self.disease.name} x {self.product.name} = {self.percent}'