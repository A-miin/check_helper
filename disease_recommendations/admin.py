from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from disease_recommendations.models import (
    DiseaseTag,
    Disease,
    Recommendation,
)

# Register your models here.


class RecommendationAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'product', 'disease', 'percent']
    list_filter = ['product', 'disease', 'author']
    search_fields = ['product__name', 'disease__name', 'author__firstname', 'author__lastname']
    readonly_fields = ('id',)
    ordering = ('-id',)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.author:
            instance.author = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance


class DiseaseAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name']
    list_filter = ['tags']
    search_fields = ['name', 'description', 'tags']
    readonly_fields = ('id',)
    ordering = ('-id',)
    list_display_links = ['name']
    filter_horizontal = ('tags',)


class DiseaseTagAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'description', 'quantity']
    list_filter = ['diseases']
    search_fields = ['name', 'description','diseases']
    readonly_fields = ('id',)
    ordering = ('-id',)
    list_display_links = ['name']
    filter_horizontal = ('diseases',)

    def quantity(self, obj):
        return Disease.objects.filter(tags=obj).count()

    quantity.short_description = _("Количество")


admin.site.register(DiseaseTag, DiseaseTagAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Recommendation, RecommendationAdmin)