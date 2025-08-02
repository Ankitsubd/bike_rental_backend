#!/usr/bin/env python3
"""
Simple script to upload local images to production backend
"""
import requests
import os
from pathlib import Path

# Production backend URL
BACKEND_URL = "https://bike-rental-backend-jmhr.onrender.com"

# Local media directory
LOCAL_MEDIA = Path("media")

def upload_images():
    """Upload local images to production"""
    if not LOCAL_MEDIA.exists():
        print("❌ Local media directory not found")
        return
    
    print("📁 Found local media directory")
    
    # List all image files
    image_files = []
    for root, dirs, files in os.walk(LOCAL_MEDIA):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                image_files.append(Path(root) / file)
    
    print(f"📸 Found {len(image_files)} image files")
    
    for image_file in image_files:
        print(f"📤 Uploading: {image_file.name}")
        # In a real scenario, you'd upload these to your production server
        # For now, just show what would be uploaded
        print(f"   → Would upload to: {BACKEND_URL}/media/{image_file.relative_to(LOCAL_MEDIA)}")

if __name__ == "__main__":
    print("🚀 Image Upload Script")
    print("=" * 30)
    upload_images()
    print("\n💡 To actually upload images:")
    print("1. Use the Django admin interface")
    print("2. Or create a proper file upload endpoint")
    print("3. Or use a cloud storage service like AWS S3") 