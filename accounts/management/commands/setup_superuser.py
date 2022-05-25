import csv
import logging

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


logger = logging.getLogger('weezer')

User = get_user_model()

class Command(BaseCommand):
    help = "Setup SuperUser"

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(email='admin@mail.com')
        user.set_password('admin')
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

