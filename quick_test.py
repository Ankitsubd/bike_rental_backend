#!/usr/bin/env python3
"""
Quick test to verify backend search and filter functionality
"""
import requests

def quick_test():
    """Quick test of the backend API"""
    
    base_url = "https://bike-rental-backend-jmhr.onrender.com/api/v1"
    
    print("🧪 Quick Backend Test")
    print("=" * 30)
    
    # Test 1: Get all bikes
    print("\n1️⃣ Testing: Get all bikes")
    try:
        response = requests.get(f"{base_url}/bikes/")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        if bikes:
            print(f"   Sample: {bikes[0].get('name', 'N/A')}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Search
    print("\n2️⃣ Testing: Search for 'Mountain'")
    try:
        response = requests.get(f"{base_url}/bikes/?search=Mountain")
        bikes = response.json()
        print(f"   Results: {len(bikes)} bikes")
        for bike in bikes[:2]:
            print(f"     - {bike.get('name', 'N/A')}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Filter
    print("\n3️⃣ Testing: Filter by type 'Mountain'")
    try:
        response = requests.get(f"{base_url}/bikes/?bike_type=Mountain")
        bikes = response.json()
        print(f"   Results: {len(bikes)} bikes")
        for bike in bikes[:2]:
            print(f"     - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n✅ Quick test completed!")

if __name__ == "__main__":
    quick_test() 