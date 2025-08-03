#!/usr/bin/env python3
"""
Test script to verify search and filter functionality
"""
import requests
import json

def test_search_filter():
    """Test the search and filter functionality"""
    
    base_url = "https://bike-rental-backend-jmhr.onrender.com/api/v1"
    
    print("🧪 Testing Search & Filter Functionality")
    print("=" * 50)
    
    # Test 1: Get all bikes
    print("\n1️⃣ Testing: Get all bikes")
    try:
        response = requests.get(f"{base_url}/bikes/")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        for bike in bikes[:3]:  # Show first 3 bikes
            print(f"   - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Search for "Mountain"
    print("\n2️⃣ Testing: Search for 'Mountain'")
    try:
        response = requests.get(f"{base_url}/bikes/?search=Mountain")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        for bike in bikes:
            print(f"   - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Filter by bike type
    print("\n3️⃣ Testing: Filter by bike_type='Mountain'")
    try:
        response = requests.get(f"{base_url}/bikes/?bike_type=Mountain")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        for bike in bikes:
            print(f"   - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Filter by status
    print("\n4️⃣ Testing: Filter by status='available'")
    try:
        response = requests.get(f"{base_url}/bikes/?status=available")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        for bike in bikes:
            print(f"   - {bike.get('name', 'N/A')} ({bike.get('status', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Combined filters
    print("\n5️⃣ Testing: Combined filters (search + status)")
    try:
        response = requests.get(f"{base_url}/bikes/?search=Mountain&status=available")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        for bike in bikes:
            print(f"   - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')} - {bike.get('status', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 6: Ordering
    print("\n6️⃣ Testing: Ordering by price")
    try:
        response = requests.get(f"{base_url}/bikes/?ordering=price_per_hour")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        for bike in bikes[:3]:
            print(f"   - {bike.get('name', 'N/A')} (${bike.get('price_per_hour', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n✅ Search & Filter tests completed!")

if __name__ == "__main__":
    test_search_filter() 