"""
Test script for FastAPI server
Verifies all SEGMENT 3 endpoints are working
"""
import requests
import time
import sys
from pathlib import Path

# Server URL
BASE_URL = "http://localhost:8000"
API_URL = f"{BASE_URL}/api/v1"

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"🧪 {text}")
    print("=" * 60 + "\n")

def test_root():
    """Test root endpoint"""
    print("1. Testing Root Endpoint (/)...")
    try:
        response = requests.get(f"{BASE_URL}/")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
        print(f"   ✅ Root endpoint working")
        print(f"   Name: {data['name']}")
        print(f"   Version: {data['version']}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def test_health():
    """Test health endpoint"""
    print("\n2. Testing Health Check (/health)...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        assert response.status_code == 200
        data = response.json()
        assert data['status'] == 'healthy'
        print(f"   ✅ Health check passed")
        print(f"   Status: {data['status']}")
        print(f"   Version: {data['version']}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def test_process_command():
    """Test command processing endpoint"""
    print("\n3. Testing Process Command (POST /api/v1/process-command)...")
    try:
        payload = {
            "text": "السلام علیکم",
            "user_id": "test_user",
            "language": "auto"
        }
        response = requests.post(f"{API_URL}/process-command", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "response_text" in data
        assert "audio_file" in data
        assert "intent" in data
        print(f"   ✅ Command processed successfully")
        print(f"   Intent: {data['intent']}")
        print(f"   Confidence: {data['confidence']}")
        print(f"   Response: {data['response_text'][:50]}...")
        print(f"   Audio: {data['audio_file']}")
        return True, data.get('audio_file')
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False, None

def test_audio(audio_filename):
    """Test audio file retrieval"""
    print("\n4. Testing Audio Retrieval (GET /api/v1/audio/{filename})...")
    if not audio_filename:
        print("   ⚠️ No audio file to test")
        return False
    
    try:
        response = requests.get(f"{API_URL}/audio/{audio_filename}")
        assert response.status_code == 200
        assert response.headers['content-type'] == 'audio/mpeg'
        print(f"   ✅ Audio file retrieved successfully")
        print(f"   File: {audio_filename}")
        print(f"   Size: {len(response.content)} bytes")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def test_commands():
    """Test commands list endpoint"""
    print("\n5. Testing Commands List (GET /api/v1/commands)...")
    try:
        response = requests.get(f"{API_URL}/commands")
        assert response.status_code == 200
        data = response.json()
        assert "commands" in data
        assert "total" in data
        print(f"   ✅ Commands retrieved successfully")
        print(f"   Total commands: {data['total']}")
        if data['commands']:
            print(f"   First command: {data['commands'][0]['category']}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def test_intents():
    """Test intents list endpoint"""
    print("\n6. Testing Intents List (GET /api/v1/intents)...")
    try:
        response = requests.get(f"{API_URL}/intents")
        assert response.status_code == 200
        data = response.json()
        assert "intents" in data
        assert "total" in data
        print(f"   ✅ Intents retrieved successfully")
        print(f"   Total intents: {data['total']}")
        print(f"   Intents: {', '.join(data['intents'][:5])}...")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def test_speech():
    """Test speech generation endpoint"""
    print("\n7. Testing Speech Generation (POST /api/v1/test-speech)...")
    try:
        params = {"text": "ہیلو دنیا", "lang": "ur"}
        response = requests.post(f"{API_URL}/test-speech", params=params)
        assert response.status_code == 200
        data = response.json()
        assert "audio_file" in data
        print(f"   ✅ Speech generated successfully")
        print(f"   Audio: {data['audio_file']}")
        print(f"   Text: {data['text']}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def test_stats():
    """Test statistics endpoint"""
    print("\n8. Testing Statistics (GET /api/v1/stats)...")
    try:
        response = requests.get(f"{API_URL}/stats")
        assert response.status_code == 200
        data = response.json()
        assert "audio_files_generated" in data
        print(f"   ✅ Statistics retrieved successfully")
        print(f"   Audio files: {data['audio_files_generated']}")
        print(f"   Total size: {data['total_audio_size_mb']} MB")
        print(f"   Supported intents: {data['supported_intents']}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False

def run_all_tests():
    """Run all API tests"""
    print_header("TESTING FASTAPI SERVER (SEGMENT 3)")
    
    # Check if server is running
    print("Checking if server is running...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=2)
        print("✅ Server is running\n")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running!")
        print("\nPlease start the server first:")
        print("   python main.py")
        print("\nOr:")
        print("   uvicorn main:app --reload")
        sys.exit(1)
    
    # Run tests
    results = {}
    
    results['root'] = test_root()
    results['health'] = test_health()
    command_result, audio_file = test_process_command()
    results['command'] = command_result
    results['audio'] = test_audio(audio_file)
    results['commands'] = test_commands()
    results['intents'] = test_intents()
    results['speech'] = test_speech()
    results['stats'] = test_stats()
    
    # Summary
    print_header("TEST RESULTS SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name.ljust(15)}: {status}")
    
    print(f"\n{'='*60}")
    print(f"Total: {passed}/{total} tests passed")
    print(f"{'='*60}")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! SEGMENT 3 IS COMPLETE!")
        print("\n✅ FastAPI server is working perfectly!")
        print("\n📖 Visit http://localhost:8000/docs for interactive API docs")
        return True
    else:
        print("\n⚠️ SOME TESTS FAILED - CHECK ERRORS ABOVE")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
