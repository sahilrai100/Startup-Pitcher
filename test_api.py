#!/usr/bin/env python3
"""
Simple test script to verify API endpoints
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

def test_api():
    print("🧪 Testing API endpoints...")
    
    # Test 1: Get top ideas
    print("\n1. Testing GET /api/top-ideas/")
    try:
        response = requests.get(f"{BASE_URL}/top-ideas/")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Found {len(data)} ideas")
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: Get all ideas
    print("\n2. Testing GET /api/ideas/")
    try:
        response = requests.get(f"{BASE_URL}/ideas/")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Found {len(data.get('results', data))} ideas")
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Register a test user
    print("\n3. Testing POST /api/auth/register/")
    try:
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123",
            "password_confirm": "testpass123",
            "first_name": "Test",
            "last_name": "User"
        }
        response = requests.post(f"{BASE_URL}/auth/register/", json=user_data)
        print(f"Status: {response.status_code}")
        if response.status_code == 201:
            print("✅ User registered successfully!")
            token = response.json().get('access')
            return token
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return None

def test_authenticated_endpoints(token):
    if not token:
        print("\n❌ No token available, skipping authenticated tests")
        return
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test 4: Submit an idea
    print("\n4. Testing POST /api/ideas/ (submit idea)")
    try:
        idea_data = {
            "title": "Test Startup Idea - AI-Powered Learning Platform",
            "description": "This is a comprehensive test idea for an AI-powered learning platform that personalizes education for each student. It uses machine learning algorithms to adapt content based on individual learning styles and progress."
        }
        response = requests.post(f"{BASE_URL}/ideas/", json=idea_data, headers=headers)
        print(f"Status: {response.status_code}")
        if response.status_code == 201:
            idea_id = response.json().get('id')
            print(f"✅ Idea created successfully! ID: {idea_id}")
            
            # Test 5: Add a comment
            print("\n5. Testing POST /api/ideas/{id}/comments/")
            comment_data = {"content": "This is a test comment on the idea!"}
            response = requests.post(f"{BASE_URL}/ideas/{idea_id}/comments/", json=comment_data, headers=headers)
            print(f"Status: {response.status_code}")
            if response.status_code == 201:
                print("✅ Comment added successfully!")
            else:
                print(f"❌ Failed: {response.text}")
                
            # Test 6: Like the idea
            print("\n6. Testing POST /api/ideas/{id}/like/")
            response = requests.post(f"{BASE_URL}/ideas/{idea_id}/like/", headers=headers)
            print(f"Status: {response.status_code}")
            if response.status_code == 201:
                print("✅ Idea liked successfully!")
            else:
                print(f"❌ Failed: {response.text}")
                
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 API Testing Script")
    print("=" * 50)
    
    token = test_api()
    test_authenticated_endpoints(token)
    
    print("\n" + "=" * 50)
    print("✅ API testing completed!")
    print("\nYour application should now be running at:")
    print("Frontend: http://localhost:3000")
    print("Backend API: http://127.0.0.1:8000/api/")
    print("Admin Panel: http://127.0.0.1:8000/admin/") 