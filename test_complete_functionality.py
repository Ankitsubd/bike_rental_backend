#!/usr/bin/env python3
"""
Comprehensive test for search and filter functionality
"""
import requests
import json
import time

def test_complete_functionality():
    """Test all search and filter functionality"""
    
    base_url = "https://bike-rental-backend-jmhr.onrender.com/api/v1"
    
    print("🧪 Comprehensive Search & Filter Test")
    print("=" * 50)
    
    # Test 1: Get all bikes
    print("\n1️⃣ Testing: Get all bikes")
    try:
        response = requests.get(f"{base_url}/bikes/")
        print(f"   Status: {response.status_code}")
        bikes = response.json()
        print(f"   Count: {len(bikes)}")
        for bike in bikes[:3]:
            print(f"   - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')})")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 2: Search functionality
    print("\n2️⃣ Testing: Search functionality")
    search_tests = [
        ("Mountain", "Search for Mountain"),
        ("Giant", "Search for Giant"),
        ("Electric", "Search for Electric"),
        ("Road", "Search for Road")
    ]
    
    for search_term, description in search_tests:
        try:
            print(f"   {description}: '{search_term}'")
            response = requests.get(f"{base_url}/bikes/?search={search_term}")
            bikes = response.json()
            print(f"   Results: {len(bikes)} bikes")
            for bike in bikes[:2]:
                print(f"     - {bike.get('name', 'N/A')}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    # Test 3: Filter by bike type
    print("\n3️⃣ Testing: Filter by bike type")
    type_tests = [
        ("Mountain", "Mountain bikes"),
        ("City ride", "City ride bikes"),
        ("Electric", "Electric bikes"),
        ("Road", "Road bikes")
    ]
    
    for bike_type, description in type_tests:
        try:
            print(f"   {description}: '{bike_type}'")
            response = requests.get(f"{base_url}/bikes/?bike_type={bike_type}")
            bikes = response.json()
            print(f"   Results: {len(bikes)} bikes")
            for bike in bikes[:2]:
                print(f"     - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')})")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    # Test 4: Filter by status
    print("\n4️⃣ Testing: Filter by status")
    status_tests = [
        ("available", "Available bikes"),
        ("booked", "Booked bikes"),
        ("in_use", "In use bikes")
    ]
    
    for status, description in status_tests:
        try:
            print(f"   {description}: '{status}'")
            response = requests.get(f"{base_url}/bikes/?status={status}")
            bikes = response.json()
            print(f"   Results: {len(bikes)} bikes")
            for bike in bikes[:2]:
                print(f"     - {bike.get('name', 'N/A')} ({bike.get('status', 'N/A')})")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    # Test 5: Combined filters
    print("\n5️⃣ Testing: Combined filters")
    combined_tests = [
        ("search=Mountain&status=available", "Mountain + Available"),
        ("search=Electric&bike_type=Electric", "Electric search + type"),
        ("bike_type=Mountain&status=available", "Mountain type + Available")
    ]
    
    for params, description in combined_tests:
        try:
            print(f"   {description}: '{params}'")
            response = requests.get(f"{base_url}/bikes/?{params}")
            bikes = response.json()
            print(f"   Results: {len(bikes)} bikes")
            for bike in bikes[:2]:
                print(f"     - {bike.get('name', 'N/A')} ({bike.get('bike_type', 'N/A')} - {bike.get('status', 'N/A')})")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    # Test 6: Ordering
    print("\n6️⃣ Testing: Ordering")
    order_tests = [
        ("price_per_hour", "Price: Low to High"),
        ("-price_per_hour", "Price: High to Low"),
        ("name", "Name: A to Z"),
        ("-name", "Name: Z to A")
    ]
    
    for order, description in order_tests:
        try:
            print(f"   {description}: '{order}'")
            response = requests.get(f"{base_url}/bikes/?ordering={order}")
            bikes = response.json()
            print(f"   Results: {len(bikes)} bikes")
            for bike in bikes[:3]:
                price = bike.get('price_per_hour', 'N/A')
                name = bike.get('name', 'N/A')
                print(f"     - {name} (${price})")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n✅ Comprehensive test completed!")
    print("\n📋 Summary:")
    print("- All API endpoints should return 200 status")
    print("- Search should return relevant results")
    print("- Filters should return filtered results")
    print("- Combined filters should work")
    print("- Ordering should sort results correctly")

if __name__ == "__main__":
    test_complete_functionality() 