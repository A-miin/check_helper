from django.contrib import admin
from disease_recommendations.models import (
    DiseaseTag,
    Disease,
    Recommendation,
)

# Register your models here.
admin.site.register(DiseaseTag)
admin.site.register(Disease)
admin.site.register(Recommendation)