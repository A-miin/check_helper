import random
from disease_recommendations.models import Recommendation, Disease
from products.models import Product


def fill_recommendations():
    for disease in Disease.objects.all():
        for i in range(10):
            product = Product.objects.order_by('?').first()
            percent = random.randint(0,100)
            recommendation = Recommendation.objects.create(
                disease=disease, product=product, percent=percent)
