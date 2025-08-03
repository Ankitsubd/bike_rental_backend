from django.core.management.base import BaseCommand
from rental_api.models import Bike
from django.core.files.base import ContentFile
import requests
from io import BytesIO

class Command(BaseCommand):
    help = 'Update bike images to use external URLs for immediate display'

    def handle(self, *args, **options):
        # External bike images (free stock photos)
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
                try:
                    # Download the image
                    response = requests.get(external_images[bike.name])
                    if response.status_code == 200:
                        # Create a file-like object
                        image_content = ContentFile(response.content)
                        # Save the image
                        bike.image.save(f'{bike.name.lower().replace(" ", "_")}.jpg', image_content, save=True)
                        self.stdout.write(f'✅ Updated {bike.name} with external image')
                        updated_count += 1
                    else:
                        self.stdout.write(f'❌ Failed to download image for {bike.name}')
                except Exception as e:
                    self.stdout.write(f'❌ Error updating {bike.name}: {str(e)}')
            else:
                self.stdout.write(f'⚠️ No external image found for: {bike.name}')
        
        self.stdout.write(self.style.SUCCESS(f'✅ Successfully updated {updated_count} bikes with external images'))
        self.stdout.write('🔄 Redeploy your backend to see the changes!') 