from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                'name': f"Listing {i}",
                'location': random.choice(['Casablanca', 'Marrakech', 'Fes']),
                'price_per_night': round(random.uniform(50, 300), 2),
                'description': f"This is Listing {i}.",
                'is_available': True,
            }
            for i in range(1, 11)
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Sample listings seeded."))

