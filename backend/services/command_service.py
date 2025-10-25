"""
Command Service - Main service that orchestrates intent detection and response generation
This is the core service that brings everything together
"""
from typing import Dict, Optional
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from services.intent_detector import IntentDetector
from services.response_generator import ResponseGenerator
from services.speech_service import SpeechService
from utils.logger import setup_logger
from utils.helpers import detect_language

logger = setup_logger(__name__)


class CommandService:
    """
    Main service for processing user commands
    Orchestrates intent detection, response generation, and speech synthesis
    """
    
    def __init__(self):
        """Initialize command service with all sub-services"""
        logger.info("🚀 Initializing CommandService...")
        
        try:
            self.intent_detector = IntentDetector()
            self.response_generator = ResponseGenerator()
            self.speech_service = SpeechService()
            
            logger.info("✅ CommandService initialized successfully with all sub-services")
        except Exception as e:
            logger.error(f"❌ Failed to initialize CommandService: {e}")
            raise
    
    async def process_command(
        self, 
        text: str, 
        user_id: Optional[str] = None,
        language_hint: str = "auto"
    ) -> Dict:
        """
        Process user command end-to-end
        
        This is the main method that:
        1. Detects intent from user text
        2. Generates appropriate response
        3. Converts response to speech
        4. Returns complete result
        
        Args:
            text: User command text (Urdu/English/mixed)
            user_id: Optional user identifier for logging/tracking
            language_hint: Language hint ('ur', 'en', or 'auto')
        
        Returns:
            Dictionary containing:
            - response_text: Generated response in Urdu
            - audio_file: Name of generated audio file
            - intent: Detected intent
            - confidence: Confidence score
            - language: Detected language
            - entities: Extracted entities
        
        Example:
            >>> service = CommandService()
            >>> result = await service.process_command("سلام")
            >>> print(result['response_text'])
            'السلام علیکم! کیا حال ہے؟'
        """
        try:
            logger.info(f"⚡ Processing command: '{text}' (user: {user_id or 'anonymous'})")
            
            # Step 1: Detect intent
            intent, confidence, entities = self.intent_detector.detect_intent(text)
            
            logger.info(f"🧠 Intent: {intent} (confidence: {confidence:.2f})")
            
            # Step 2: Generate response
            response_text = self.response_generator.generate_response(
                intent=intent,
                confidence=confidence,
                entities=entities
            )
            
            logger.info(f"💬 Response: {response_text[:50]}...")
            
            # Step 3: Detect language for speech synthesis
            if language_hint == "auto":
                detected_lang = detect_language(response_text)
                # Convert 'mixed' to 'ur' for speech (gTTS handles Urdu best)
                speech_lang = 'ur' if detected_lang in ['ur', 'mixed'] else 'en'
            else:
                speech_lang = language_hint if language_hint in ['ur', 'en'] else 'ur'
            
            # Step 4: Convert to speech
            audio_filename = None
            try:
                audio_filename = self.speech_service.text_to_speech(
                    text=response_text,
                    lang=speech_lang
                )
                logger.info(f"🎤 Audio generated: {audio_filename}")
            except Exception as e:
                logger.error(f"❌ Speech generation failed: {e}")
                # Continue without audio - not critical
            
            # Step 5: Prepare result
            result = {
                'response_text': response_text,
                'audio_file': audio_filename,
                'intent': intent,
                'confidence': round(confidence, 2),
                'language': speech_lang,
                'entities': entities
            }
            
            logger.info(f"✅ Command processed successfully: {intent}")
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Command processing failed: {e}", exc_info=True)
            
            # Return error response
            return self._get_error_result()
    
    def _get_error_result(self) -> Dict:
        """
        Get error result when command processing fails
        
        Returns:
            Error result dictionary
        """
        error_response = "معاف کیجیے، کچھ غلطی ہو گئی۔ دوبارہ کوشش کریں۔"
        
        # Try to generate error audio
        audio_filename = None
        try:
            audio_filename = self.speech_service.text_to_speech(
                text=error_response,
                lang='ur'
            )
        except:
            logger.warning("⚠️ Could not generate error audio")
        
        return {
            'response_text': error_response,
            'audio_file': audio_filename,
            'intent': 'error',
            'confidence': 0.0,
            'language': 'ur',
            'entities': {}
        }
    
    def get_available_commands(self) -> Dict:
        """
        Get list of all available commands/intents
        
        Returns:
            Dictionary with commands information
        
        Example:
            >>> service.get_available_commands()
            {
                'total': 11,
                'intents': ['greeting', 'farewell', 'weather', ...],
                'message': 'دستیاب کمانڈز'
            }
        """
        try:
            intents = self.intent_detector.get_all_intents()
            
            return {
                'total': len(intents),
                'intents': sorted(intents),
                'message': 'دستیاب کمانڈز',
                'status': 'success'
            }
        except Exception as e:
            logger.error(f"❌ Failed to get commands: {e}")
            return {
                'total': 0,
                'intents': [],
                'message': 'خرابی',
                'status': 'error'
            }
    
    def get_service_status(self) -> Dict:
        """
        Get status of all sub-services
        
        Returns:
            Dictionary with service status information
        """
        try:
            return {
                'command_service': 'healthy',
                'intent_detector': 'healthy' if self.intent_detector else 'unavailable',
                'response_generator': 'healthy' if self.response_generator else 'unavailable',
                'speech_service': 'healthy' if self.speech_service else 'unavailable',
                'total_intents': len(self.intent_detector.get_all_intents()),
                'status': 'operational'
            }
        except Exception as e:
            logger.error(f"❌ Status check failed: {e}")
            return {
                'status': 'degraded',
                'error': str(e)
            }


# Test the command service
if __name__ == "__main__":
    import asyncio
    
    print("🧪 Testing CommandService...\n")
    
    async def test_command_service():
        try:
            service = CommandService()
            
            # Test cases
            test_commands = [
                "السلام علیکم",
                "وقت کیا ہوا ہے؟",
                "موسم کیسا ہے؟",
                "کوئی لطیفہ سناؤ",
                "اللہ حافظ",
            ]
            
            print("Testing command processing:\n")
            for i, command in enumerate(test_commands, 1):
                print(f"{i}. Processing: '{command}'")
                result = await service.process_command(command)
                print(f"   Intent: {result['intent']} (confidence: {result['confidence']})")
                print(f"   Response: {result['response_text']}")
                print(f"   Audio: {result['audio_file']}")
                print(f"   Language: {result['language']}")
                print()
            
            # Test service status
            print("\nService Status:")
            status = service.get_service_status()
            for key, value in status.items():
                print(f"   {key}: {value}")
            
            # Test available commands
            print("\nAvailable Commands:")
            commands = service.get_available_commands()
            print(f"   Total: {commands['total']}")
            print(f"   Intents: {', '.join(commands['intents'])}")
            
            print("\n✅ All CommandService tests completed!")
            
        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            import traceback
            traceback.print_exc()
    
    # Run async test
    asyncio.run(test_command_service())
