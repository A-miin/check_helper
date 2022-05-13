from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe, format_html

from products.models import Product, ProductCategory


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'category', 'name', 'image', 'price', 'description', 'qr_code', 'uuid']
    list_filter = ['category']
    search_fields = ['name', 'description']
    readonly_fields = ('id',)
    ordering = ('-id',)
    list_display_links = ['name']

    def image(self, obj):
        return format_html(
            f'''
            <img alt="{_("Фото")}" src="{obj.photo_link}"
                    width=70" height="70">
            '''
        )

    image.short_description = _("Фото")

    def qr_code(self,obj):
        return mark_safe(
            f"""
      <img id='barcode'
            src="https://api.qrserver.com/v1/create-qr-code/?data={obj.uuid}&amp;size=100x100"
            alt=""
            title="HELLO"
            width="50"
            height="50" />
            """
        )


class ProductCategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'image', 'quantity']
    search_fields = ['name']
    readonly_fields = ('id',)
    ordering = ('-id',)
    list_display_links = ['name']

    def quantity(self, obj):
        return Product.objects.filter(category=obj).count()

    quantity.short_description = _("Количество")

    def image(self, obj):
        return format_html(
            f'''
            <img alt="{_("Фото")}" src="{obj.photo_link}"
                    width=70" height="70">
            '''
        )

    image.short_description = _("Фото")


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
