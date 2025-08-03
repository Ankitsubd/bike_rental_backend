#!/usr/bin/env python3
"""
Fix Cloudinary image issues by updating bikes to use external URLs
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from rental_api.models import Bike

def fix_cloudinary_images():
    """Update bikes to use external URLs instead of broken Cloudinary URLs"""
    
    # External image URLs (free stock photos)
    external_images = {
        'Giant 6000': 'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=300&fit=crop',
        'Adriatica Tourenrad Retro': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
        'Hiland Mountain': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
        'BSA Girl\'s Sofiaa': 'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=300&fit=crop',
        'Mountain Bike': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
    }
    
    print("🔧 Fixing Cloudinary Image Issues")
    print("=" * 40)
    
    bikes = Bike.objects.all()
    updated_count = 0
    
    for bike in bikes:
        print(f"🚴 {bike.name}:")
        
        # Clear the broken Cloudinary field
        if bike.image:
            print(f"   ❌ Removing broken Cloudinary URL: {bike.image}")
            bike.image = None
        
        # Set external URL
        if bike.name in external_images:
            bike.image_url = external_images[bike.name]
            print(f"   ✅ Setting external URL: {bike.image_url}")
            updated_count += 1
        else:
            print(f"   ⚠️ No external image found for {bike.name}")
        
        bike.save()
        print()
    
    print(f"🎉 Fixed {updated_count} bikes!")
    print("\n📋 Summary:")
    print("- Removed broken Cloudinary URLs")
    print("- Set external image URLs")
    print("- Images should now display correctly")
    
    return updated_count

if __name__ == "__main__":
    fix_cloudinary_images() 