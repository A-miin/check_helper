from django.contrib import admin
from disease_recommendations.models import (
    DiseaseCategory,
    Disease,
    Recommendation,
)

# Register your models here.
admin.site.register(DiseaseCategory)
admin.site.register(Disease)
admin.site.register(Recommendation)