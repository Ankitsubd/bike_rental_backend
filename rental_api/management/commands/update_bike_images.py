from django.core.management.base import BaseCommand
from rental_api.models import Bike

class Command(BaseCommand):
    help = 'Update bike images to use external URLs'

    def handle(self, *args, **options):
        # Sample external bike images (you can replace these with your own)
        external_images = {
            'Giant 6000': 'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=300&fit=crop',
            'Adriatica Tourenrad Retro': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
            'Hiland Mountain': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
            'BSA Girl\'s Sofiaa': 'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=300&fit=crop',
            'Mountain Bike': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
        }
        
        bikes = Bike.objects.all()
        updated_count = 0
        
        for bike in bikes:
            if bike.name in external_images:
                # For now, we'll just print what would be updated
                # In a real scenario, you'd need to modify the model to support URL fields
                self.stdout.write(f'Would update {bike.name} to use: {external_images[bike.name]}')
                updated_count += 1
            else:
                self.stdout.write(f'No external image found for: {bike.name}')
        
        self.stdout.write(self.style.SUCCESS(f'Found {updated_count} bikes to update'))
        self.stdout.write(self.style.WARNING('Note: This is a preview. To actually update, you need to modify the Bike model to support URL fields.')) 