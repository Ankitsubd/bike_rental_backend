#!/usr/bin/env python3
"""
Test script to verify backend filtering functionality
"""
import os
import django
import requests

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from rental_api.models import Bike

def test_backend_filters():
    """Test the backend filtering functionality"""
    
    print("🧪 Testing Backend Filters")
    print("=" * 40)
    
    # Test 1: Get all bikes
    print("\n1️⃣ Testing: Get all bikes")
    response = requests.get('http://localhost:8000/api/v1/bikes/')
    print(f"   Status: {response.status_code}")
    print(f"   Count: {len(response.json())}")
    
    # Test 2: Search for "Mountain"
    print("\n2️⃣ Testing: Search for 'Mountain'")
    response = requests.get('http://localhost:8000/api/v1/bikes/?search=Mountain')
    print(f"   Status: {response.status_code}")
    print(f"   Count: {len(response.json())}")
    
    # Test 3: Filter by bike type
    print("\n3️⃣ Testing: Filter by bike_type='Mountain'")
    response = requests.get('http://localhost:8000/api/v1/bikes/?bike_type=Mountain')
    print(f"   Status: {response.status_code}")
    print(f"   Count: {len(response.json())}")
    
    # Test 4: Filter by status
    print("\n4️⃣ Testing: Filter by status='available'")
    response = requests.get('http://localhost:8000/api/v1/bikes/?status=available')
    print(f"   Status: {response.status_code}")
    print(f"   Count: {len(response.json())}")
    
    # Test 5: Combined filters
    print("\n5️⃣ Testing: Combined filters")
    response = requests.get('http://localhost:8000/api/v1/bikes/?search=Mountain&status=available')
    print(f"   Status: {response.status_code}")
    print(f"   Count: {len(response.json())}")
    
    print("\n✅ Backend filter tests completed!")

if __name__ == "__main__":
    test_backend_filters() 