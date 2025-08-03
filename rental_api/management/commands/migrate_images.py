from django.core.management.base import BaseCommand
from rental_api.models import Bike
import os
from django.conf import settings

try:
    import cloudinary.uploader
    CLOUDINARY_AVAILABLE = True
except ImportError:
    CLOUDINARY_AVAILABLE = False

class Command(BaseCommand):
    help = 'Migrate existing local images to Cloudinary'

    def handle(self, *args, **options):
        if not CLOUDINARY_AVAILABLE:
            self.stdout.write(
                self.style.ERROR('❌ Cloudinary is not available. Please install it first.')
            )
            return
            
        bikes = Bike.objects.all()
        migrated_count = 0
        skipped_count = 0
        
        for bike in bikes:
            try:
                # Check if bike has a local image file
                if bike.image and hasattr(bike.image, 'path') and os.path.exists(bike.image.path):
                    self.stdout.write(f'Migrating image for bike: {bike.name}')
                    
                    # Upload to Cloudinary
                    result = cloudinary.uploader.upload(
                        bike.image.path,
                        folder="bikes",
                        public_id=f"{bike.name.lower().replace(' ', '_')}",
                        overwrite=True
                    )
                    
                    # Update the bike with Cloudinary URL
                    bike.image = result['secure_url']
                    bike.save()
                    
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ Successfully migrated {bike.name} to Cloudinary')
                    )
                    migrated_count += 1
                    
                elif bike.image_url:
                    self.stdout.write(f'⏭️ Skipping {bike.name} - already has external URL')
                    skipped_count += 1
                    
                else:
                    self.stdout.write(f'⚠️ No image found for {bike.name}')
                    skipped_count += 1
                    
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Error migrating {bike.name}: {str(e)}')
                )
                skipped_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n🎉 Migration complete!\n'
                f'✅ Migrated: {migrated_count} images\n'
                f'⏭️ Skipped: {skipped_count} images'
            )
        ) 