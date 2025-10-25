"""
Response Generator Service - Generate appropriate responses based on intent
Creates natural Urdu responses with context awareness
"""
import random
from typing import Dict, Optional, List
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import RESPONSES_FILE, JOKES_FILE
from utils.logger import setup_logger
from utils.helpers import (
    load_json_file, 
    get_current_time_urdu, 
    get_current_date_urdu
)

logger = setup_logger(__name__)


class ResponseGenerator:
    """
    Generate appropriate Urdu responses based on detected intent
    Uses templates from JSON files with dynamic content insertion
    """
    
    def __init__(self):
        """Initialize response generator with templates"""
        self.responses = self._load_responses()
        self.jokes = self._load_jokes()
        logger.info(f"✅ ResponseGenerator initialized with {len(self.responses)} response categories")
    
    def _load_responses(self) -> Dict:
        """
        Load response templates from JSON file
        
        Returns:
            Dictionary of response templates
        """
        try:
            responses = load_json_file(RESPONSES_FILE)
            if not responses:
                logger.warning("⚠️ No responses found, using defaults")
                return self._get_default_responses()
            return responses
        except Exception as e:
            logger.error(f"❌ Failed to load responses: {e}")
            return self._get_default_responses()
    
    def _load_jokes(self) -> Dict:
        """
        Load jokes from JSON file
        
        Returns:
            Dictionary containing jokes list
        """
        try:
            jokes = load_json_file(JOKES_FILE)
            if not jokes or 'jokes' not in jokes:
                logger.warning("⚠️ No jokes found, using defaults")
                return {"jokes": [{"text": "معاف کیجیے، کوئی لطیفہ یاد نہیں آ رہا!"}]}
            return jokes
        except Exception as e:
            logger.error(f"❌ Failed to load jokes: {e}")
            return {"jokes": [{"text": "معاف کیجیے، کوئی لطیفہ یاد نہیں آ رہا!"}]}
    
    def _get_default_responses(self) -> Dict:
        """
        Get default responses if file loading fails
        
        Returns:
            Dictionary of basic default responses
        """
        return {
            "greeting": ["السلام علیکم! کیا حال ہے؟"],
            "farewell": ["اللہ حافظ! دوبارہ ضرور آئیں۔"],
            "unknown": ["معاف کیجیے، میں سمجھ نہیں پایا۔"],
            "error": ["کچھ غلطی ہو گئی۔ دوبارہ کوشش کریں۔"]
        }
    
    def generate_response(
        self, 
        intent: str, 
        confidence: float, 
        entities: Optional[Dict] = None
    ) -> str:
        """
        Generate appropriate response based on intent
        
        Args:
            intent: Detected intent name
            confidence: Confidence score (0.0 to 1.0)
            entities: Extracted entities (optional)
        
        Returns:
            Response text in Urdu
        
        Example:
            >>> generator = ResponseGenerator()
            >>> response = generator.generate_response('greeting', 0.95, {})
            >>> print(response)
            'السلام علیکم! کیا حال ہے؟'
        """
        try:
            entities = entities or {}
            
            logger.debug(f"💬 Generating response for intent: {intent}")
            
            # Route to specific handler based on intent
            handlers = {
                'greeting': self._handle_greeting,
                'farewell': self._handle_farewell,
                'thanks': self._handle_thanks,
                'how_are_you': self._handle_how_are_you,
                'weather': self._handle_weather,
                'time': self._handle_time,
                'date': self._handle_date,
                'prayer': self._handle_prayer,
                'joke': self._handle_joke,
                'news': self._handle_news,
                'help': self._handle_help,
                'unknown': self._handle_unknown
            }
            
            # Get handler or default to unknown
            handler = handlers.get(intent, self._handle_unknown)
            
            # Generate response
            response = handler(entities)
            
            logger.info(f"✅ Response generated for {intent}: {response[:50]}...")
            
            return response
            
        except Exception as e:
            logger.error(f"❌ Response generation failed: {e}", exc_info=True)
            return self._get_error_response()
    
    def _handle_greeting(self, entities: Dict) -> str:
        """Handle greeting intent"""
        responses = self.responses.get('greeting', ["السلام علیکم!"])
        return random.choice(responses)
    
    def _handle_farewell(self, entities: Dict) -> str:
        """Handle farewell intent"""
        responses = self.responses.get('farewell', ["اللہ حافظ!"])
        return random.choice(responses)
    
    def _handle_thanks(self, entities: Dict) -> str:
        """Handle thanks intent"""
        responses = self.responses.get('thanks', ["کوئی بات نہیں!"])
        return random.choice(responses)
    
    def _handle_how_are_you(self, entities: Dict) -> str:
        """Handle 'how are you' intent"""
        responses = self.responses.get('how_are_you', [
            "میں بالکل ٹھیک ہوں، شکریہ! آپ کیسے ہیں؟"
        ])
        return random.choice(responses)
    
    def _handle_weather(self, entities: Dict) -> str:
        """
        Handle weather query (mock data)
        Includes city name if provided in entities
        """
        responses = self.responses.get('weather_mock', ["آج موسم اچھا ہے!"])
        response = random.choice(responses)
        
        # Add city if provided in entities
        if 'city' in entities:
            city_names = {
                'karachi': 'کراچی',
                'lahore': 'لاہور',
                'islamabad': 'اسلام آباد',
                'peshawar': 'پشاور',
                'quetta': 'کوئٹہ',
                'multan': 'ملتان',
                'faisalabad': 'فیصل آباد',
                'rawalpindi': 'راولپنڈی'
            }
            city = entities['city']
            city_urdu = city_names.get(city, city)
            response = f"{city_urdu} میں {response}"
        
        return response
    
    def _handle_time(self, entities: Dict) -> str:
        """
        Handle time query
        Returns current time in Urdu format
        """
        try:
            time_urdu = get_current_time_urdu()
            return time_urdu
        except Exception as e:
            logger.error(f"❌ Failed to get time: {e}")
            return "معاف کیجیے، وقت معلوم نہیں ہو سکا۔"
    
    def _handle_date(self, entities: Dict) -> str:
        """
        Handle date query
        Returns current date in Urdu format
        """
        try:
            date_urdu = get_current_date_urdu()
            return date_urdu
        except Exception as e:
            logger.error(f"❌ Failed to get date: {e}")
            return "معاف کیجیے، تاریخ معلوم نہیں ہو سکی۔"
    
    def _handle_prayer(self, entities: Dict) -> str:
        """
        Handle prayer time query (mock data)
        Can include specific prayer name if provided
        """
        responses = self.responses.get('prayer_mock', ["نماز کا وقت آ گیا ہے۔"])
        
        # If specific prayer requested, try to give more specific response
        if 'prayer_name' in entities:
            prayer_name = entities['prayer_name']
            prayer_responses = {
                'fajr': "فجر کی نماز صبح 5:30 بجے ہے۔",
                'zuhr': "ظہر کی نماز دوپہر 1:30 بجے ہے۔",
                'asr': "عصر کی نماز شام 5:00 بجے ہے۔",
                'maghrib': "مغرب کی نماز شام 6:30 بجے ہے۔",
                'isha': "عشاء کی نماز رات 8:00 بجے ہے۔"
            }
            return prayer_responses.get(prayer_name, random.choice(responses))
        
        return random.choice(responses)
    
    def _handle_joke(self, entities: Dict) -> str:
        """
        Handle joke request
        Returns random Urdu joke
        """
        jokes_list = self.jokes.get('jokes', [])
        
        if not jokes_list:
            return "معاف کیجیے، کوئی لطیفہ یاد نہیں آ رہا!"
        
        # Get random joke
        joke = random.choice(jokes_list)
        
        # Extract text from joke object or use directly if string
        if isinstance(joke, dict):
            return joke.get('text', "کوئی لطیفہ نہیں ملا!")
        else:
            return str(joke)
    
    def _handle_news(self, entities: Dict) -> str:
        """Handle news request (mock data)"""
        responses = self.responses.get('news_mock', ["آج کوئی خاص خبر نہیں ہے۔"])
        return random.choice(responses)
    
    def _handle_help(self, entities: Dict) -> str:
        """
        Handle help request
        Provides information about available commands
        """
        responses = self.responses.get('help', [
            "میں موسم، وقت، تاریخ، نماز کے اوقات، لطیفے، اور خبریں بتا سکتا ہوں۔"
        ])
        return random.choice(responses)
    
    def _handle_unknown(self, entities: Dict) -> str:
        """Handle unknown intent"""
        responses = self.responses.get('unknown', ["معاف کیجیے، میں سمجھ نہیں پایا۔"])
        return random.choice(responses)
    
    def _get_error_response(self) -> str:
        """Get error response"""
        responses = self.responses.get('error', ["کچھ غلطی ہو گئی۔"])
        return random.choice(responses)
    
    def get_response_categories(self) -> List[str]:
        """
        Get list of all response categories
        
        Returns:
            List of category names
        """
        return list(self.responses.keys())
    
    def add_responses(self, category: str, responses: List[str]):
        """
        Add new response templates dynamically
        
        Args:
            category: Response category name
            responses: List of response templates
        
        Example:
            >>> generator.add_responses('birthday', ['جنم دن مبارک!', 'سالگرہ مبارک ہو!'])
        """
        if category not in self.responses:
            self.responses[category] = []
        self.responses[category].extend(responses)
        logger.info(f"✅ Added {len(responses)} responses to category: {category}")


# Test the generator
if __name__ == "__main__":
    print("🧪 Testing ResponseGenerator...\n")
    
    generator = ResponseGenerator()
    
    # Test cases
    test_cases = [
        ('greeting', 0.95, {}),
        ('farewell', 0.90, {}),
        ('time', 0.92, {}),
        ('date', 0.92, {}),
        ('weather', 0.88, {'city': 'karachi'}),
        ('prayer', 0.90, {'prayer_name': 'fajr'}),
        ('joke', 0.85, {}),
        ('help', 0.90, {}),
        ('unknown', 0.30, {}),
    ]
    
    print("Testing response generation:\n")
    for i, (intent, confidence, entities) in enumerate(test_cases, 1):
        response = generator.generate_response(intent, confidence, entities)
        print(f"{i}. Intent: {intent} (confidence: {confidence})")
        print(f"   Response: {response}")
        print()
    
    print(f"✅ Response categories: {generator.get_response_categories()}")
