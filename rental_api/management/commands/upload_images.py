from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
import os
from pathlib import Path

class Command(BaseCommand):
    help = 'Upload local images to production media directory'

    def handle(self, *args, **options):
        # Local media directory
        local_media = Path(settings.BASE_DIR) / 'media'
        
        # Production media directory
        prod_media = Path(settings.MEDIA_ROOT)
        
        self.stdout.write(f'Local media path: {local_media}')
        self.stdout.write(f'Production media path: {prod_media}')
        
        if not local_media.exists():
            self.stdout.write(self.style.ERROR('Local media directory not found'))
            return
            
        # Create production media directory if it doesn't exist
        prod_media.mkdir(parents=True, exist_ok=True)
        
        # Copy all files from local to production
        for root, dirs, files in os.walk(local_media):
            # Get relative path from local media
            rel_path = Path(root).relative_to(local_media)
            prod_path = prod_media / rel_path
            
            # Create directory in production
            prod_path.mkdir(parents=True, exist_ok=True)
            
            for file in files:
                local_file = Path(root) / file
                prod_file = prod_path / file
                
                # Copy file
                with open(local_file, 'rb') as f:
                    with open(prod_file, 'wb') as pf:
                        pf.write(f.read())
                
                self.stdout.write(f'Uploaded: {file}')
        
        self.stdout.write(self.style.SUCCESS('All images uploaded successfully!')) 