from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name=_('Название'),
        null=True,
        max_length=128,
    )
    photo_link = models.URLField(
        verbose_name=_('Ссылка на фотографию'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('Категория продуктов')
        verbose_name_plural = _('Категории продуктов')

    def __str__(self):
        return self.name


class Product(models.Model):

    uuid = models.CharField(
        verbose_name=_('uuid'),
        unique=True,
        blank=True,
        max_length=64,
    )
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=256,
    )
    photo_link = models.URLField(
        verbose_name=_('Ссылка на фотографию'),
        blank=True,
        null=True,
    )
    qr = models.IntegerField(
        verbose_name=_('QR код'),
        blank=True,
        null=True,
    )
    description = models.CharField(
        verbose_name=_('Описание'),
        max_length=1024,
        blank=True,
    )
    price = models.FloatField(
        verbose_name=_('Средняя цена'),
        default=0,
    )
    category = models.ForeignKey(
        'products.ProductCategory',
        on_delete=models.CASCADE,
        related_name='products',
    )

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        while True:
            uuid = uuid4()
            if not Product.objects.filter(uuid=uuid).exists():
                self.uuid = uuid
                break
        super(Product, self).save(*args, **kwargs)