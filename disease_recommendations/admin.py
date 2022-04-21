from django.contrib import admin
from disease_recommendations.models import (
    DiseaseTag,
    Disease,
    Recommendation,
)

# Register your models here.


class RecommendationAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.author:
            instance.author = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(DiseaseTag)
admin.site.register(Disease)
admin.site.register(Recommendation, RecommendationAdmin)