#!/usr/bin/env python3
"""
Manual script to fix bike images
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from rental_api.models import Bike

def fix_bike_images():
    """Update bike images to use external URLs"""
    
    # External image URLs (free stock photos)
    image_urls = {
        'Giant 6000': 'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=300&fit=crop',
        'Adriatica Tourenrad Retro': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
        'Hiland Mountain': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
        'BSA Girl\'s Sofiaa': 'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=300&fit=crop',
        'Mountain Bike': 'https://images.unsplash.com/photo-1544191696-102dbdaeeaa1?w=400&h=300&fit=crop',
    }
    
    print("🚴 Fixing Bike Images")
    print("=" * 30)
    
    bikes = Bike.objects.all()
    for bike in bikes:
        print(f"📸 {bike.name}:")
        if bike.name in image_urls:
            print(f"   ✅ External URL: {image_urls[bike.name]}")
            print(f"   💡 To fix: Update this bike in Django admin")
        else:
            print(f"   ⚠️ No external image found")
        print()
    
    print("🔧 To fix images:")
    print("1. Go to: https://bike-rental-backend-jmhr.onrender.com/admin/")
    print("2. Login with admin credentials")
    print("3. Go to 'Bikes' section")
    print("4. Edit each bike and upload new images")
    print("5. Or use the external URLs above")

if __name__ == "__main__":
    fix_bike_images() 