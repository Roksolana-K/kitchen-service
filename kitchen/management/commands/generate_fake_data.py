from django.core.management.base import BaseCommand
from fake_data import generate_fake_data

class Command(BaseCommand):
    help = 'Generate fake data for the kitchen project'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to generate fake data...")
        generate_fake_data()
        self.stdout.write(self.style.SUCCESS("Fake data generated successfully!"))
