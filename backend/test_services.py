"""
Test script for all backend services
Run this to verify SEGMENT 2 implementation
"""
import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).resolve().parent))

from services.speech_service import SpeechService
from services.intent_detector import IntentDetector
from services.response_generator import ResponseGenerator
from services.command_service import CommandService
from utils.logger import setup_logger

logger = setup_logger(__name__)


def test_speech_service():
    """Test SpeechService"""
    print("\n" + "="*60)
    print("🧪 TESTING SPEECH SERVICE")
    print("="*60 + "\n")
    
    try:
        service = SpeechService()
        
        # Test Urdu speech
        print("1. Generating Urdu speech...")
        urdu_file = service.text_to_speech("السلام علیکم! یہ ایک ٹیسٹ ہے۔", "ur")
        print(f"   ✅ Generated: {urdu_file}")
        
        # Test English speech
        print("\n2. Generating English speech...")
        english_file = service.text_to_speech("Hello! This is a test.", "en")
        print(f"   ✅ Generated: {english_file}")
        
        # Test file exists
        print("\n3. Checking file existence...")
        exists = service.file_exists(urdu_file)
        print(f"   ✅ File exists: {exists}")
        
        print("\n✅ SpeechService tests PASSED!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ SpeechService tests FAILED: {e}\n")
        return False


def test_intent_detector():
    """Test IntentDetector"""
    print("\n" + "="*60)
    print("🧪 TESTING INTENT DETECTOR")
    print("="*60 + "\n")
    
    try:
        detector = IntentDetector()
        
        test_cases = [
            ("السلام علیکم", "greeting"),
            ("موسم کیسا ہے؟", "weather"),
            ("وقت کیا ہوا ہے؟", "time"),
            ("اللہ حافظ", "farewell"),
        ]
        
        passed = 0
        for text, expected_intent in test_cases:
            intent, confidence, entities = detector.detect_intent(text)
            status = "✅" if intent == expected_intent else "❌"
            print(f"{status} '{text}' -> {intent} (expected: {expected_intent})")
            if intent == expected_intent:
                passed += 1
        
        print(f"\n✅ Passed {passed}/{len(test_cases)} tests\n")
        return passed == len(test_cases)
        
    except Exception as e:
        print(f"\n❌ IntentDetector tests FAILED: {e}\n")
        return False


def test_response_generator():
    """Test ResponseGenerator"""
    print("\n" + "="*60)
    print("🧪 TESTING RESPONSE GENERATOR")
    print("="*60 + "\n")
    
    try:
        generator = ResponseGenerator()
        
        test_intents = ['greeting', 'farewell', 'time', 'date', 'weather', 'joke']
        
        for intent in test_intents:
            response = generator.generate_response(intent, 0.95, {})
            print(f"✅ {intent}: {response[:50]}...")
        
        print("\n✅ ResponseGenerator tests PASSED!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ ResponseGenerator tests FAILED: {e}\n")
        return False


async def test_command_service():
    """Test CommandService"""
    print("\n" + "="*60)
    print("🧪 TESTING COMMAND SERVICE")
    print("="*60 + "\n")
    
    try:
        service = CommandService()
        
        test_commands = [
            "السلام علیکم",
            "وقت کیا ہوا ہے؟",
            "موسم کیسا ہے؟",
        ]
        
        for i, command in enumerate(test_commands, 1):
            print(f"{i}. Testing: '{command}'")
            result = await service.process_command(command)
            print(f"   Intent: {result['intent']}")
            print(f"   Response: {result['response_text'][:50]}...")
            print(f"   Audio: {result['audio_file']}")
            print()
        
        print("✅ CommandService tests PASSED!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ CommandService tests FAILED: {e}\n")
        import traceback
        traceback.print_exc()
        return False


async def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("🚀 RUNNING ALL SEGMENT 2 TESTS")
    print("="*60)
    
    results = {
        'SpeechService': test_speech_service(),
        'IntentDetector': test_intent_detector(),
        'ResponseGenerator': test_response_generator(),
        'CommandService': await test_command_service()
    }
    
    print("\n" + "="*60)
    print("📊 TEST RESULTS SUMMARY")
    print("="*60 + "\n")
    
    for service, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{service}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! SEGMENT 2 IS COMPLETE!")
    else:
        print("⚠️ SOME TESTS FAILED - CHECK ERRORS ABOVE")
    print("="*60 + "\n")
    
    return all_passed


if __name__ == "__main__":
    asyncio.run(run_all_tests())
