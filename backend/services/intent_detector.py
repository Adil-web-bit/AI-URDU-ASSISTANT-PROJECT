"""
Intent Detector Service - Classify user intents using pattern matching
Uses regex-based NLP for accurate intent detection in Urdu/English
"""
import re
from typing import Dict, List, Tuple
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import PATTERNS_FILE
from utils.logger import setup_logger
from utils.helpers import load_json_file, clean_text

logger = setup_logger(__name__)


class IntentDetector:
    """
    Detect user intent from text using keyword pattern matching
    Supports both Urdu and English with high accuracy
    """
    
    def __init__(self):
        """Initialize intent detector with patterns from JSON"""
        self.patterns = self._load_patterns()
        logger.info(f"✅ IntentDetector initialized with {len(self.patterns)} intent patterns")
    
    def _load_patterns(self) -> Dict:
        """
        Load intent patterns from JSON file
        
        Returns:
            Dictionary of intent patterns
        """
        try:
            patterns = load_json_file(PATTERNS_FILE)
            if not patterns or 'patterns' not in patterns:
                logger.warning("⚠️ No patterns found in patterns.json, using defaults")
                return self._get_default_patterns()
            return patterns['patterns']
        except Exception as e:
            logger.error(f"❌ Failed to load patterns: {e}")
            return self._get_default_patterns()
    
    def _get_default_patterns(self) -> Dict:
        """
        Get default patterns if file loading fails
        
        Returns:
            Dictionary of basic default patterns
        """
        return {
            "greeting": {
                "keywords": ["سلام", "hello", "hi", "آداب", "assalam"],
                "confidence": 0.95
            },
            "farewell": {
                "keywords": ["bye", "alvida", "حافظ", "goodbye"],
                "confidence": 0.95
            },
            "unknown": {
                "keywords": [],
                "confidence": 0.0
            }
        }
    
    def detect_intent(self, text: str) -> Tuple[str, float, Dict]:
        """
        Detect intent from user text using keyword matching
        
        Args:
            text: User input text (Urdu/English/mixed)
        
        Returns:
            Tuple of (intent_name, confidence_score, entities)
            - intent_name: Detected intent (e.g., 'greeting', 'weather', 'time')
            - confidence_score: Confidence between 0.0 and 1.0
            - entities: Extracted entities (dict)
        
        Example:
            >>> detector = IntentDetector()
            >>> intent, conf, entities = detector.detect_intent("سلام، کیا حال ہے؟")
            >>> print(intent, conf)
            'greeting' 0.95
        """
        try:
            # Clean and normalize text
            cleaned_text = clean_text(text).lower()
            
            if not cleaned_text:
                logger.warning("⚠️ Empty text provided")
                return ('unknown', 0.0, {})
            
            logger.debug(f"🔍 Detecting intent for: {cleaned_text}")
            
            # Check each intent pattern
            best_intent = 'unknown'
            best_confidence = 0.0
            best_matches = 0
            
            for intent_name, pattern_data in self.patterns.items():
                keywords = pattern_data.get('keywords', [])
                base_confidence = pattern_data.get('confidence', 0.5)
                
                if not keywords:
                    continue
                
                # Count matching keywords
                matches = 0
                matched_keywords = []
                
                for keyword in keywords:
                    keyword_lower = keyword.lower()
                    # Use word boundary regex for better matching
                    # This prevents partial matches (e.g., 'hi' in 'this')
                    pattern = rf'\b{re.escape(keyword_lower)}\b'
                    
                    if re.search(pattern, cleaned_text, re.IGNORECASE):
                        matches += 1
                        matched_keywords.append(keyword)
                
                # Calculate confidence based on matches
                if matches > 0:
                    # More matches = higher confidence
                    # Formula: base_confidence * (matches / sqrt(total_keywords))
                    # This rewards multiple matches without penalizing intents with many keywords
                    match_ratio = min(1.0, matches / max(1, len(keywords) ** 0.5))
                    match_confidence = base_confidence * (0.5 + 0.5 * match_ratio)
                    
                    # Update best match if this is better
                    if match_confidence > best_confidence:
                        best_intent = intent_name
                        best_confidence = match_confidence
                        best_matches = matches
                    # If confidence is same, prefer more matches
                    elif match_confidence == best_confidence and matches > best_matches:
                        best_intent = intent_name
                        best_matches = matches
                    
                    logger.debug(f"  Intent '{intent_name}': {matches} matches, confidence: {match_confidence:.2f}")
            
            # Extract entities from text
            entities = self._extract_entities(cleaned_text, best_intent)
            
            logger.info(f"✅ Intent detected: {best_intent} (confidence: {best_confidence:.2f})")
            
            return (best_intent, best_confidence, entities)
            
        except Exception as e:
            logger.error(f"❌ Intent detection failed: {e}", exc_info=True)
            return ('unknown', 0.0, {})
    
    def _extract_entities(self, text: str, intent: str) -> Dict:
        """
        Extract entities from text based on intent
        
        Args:
            text: Cleaned user text (lowercase)
            intent: Detected intent
        
        Returns:
            Dictionary of extracted entities
        
        Note: This is a basic implementation using regex.
              Can be enhanced with NER models in future.
        """
        entities = {}
        
        try:
            # Extract numbers (useful for many intents)
            numbers = re.findall(r'\d+', text)
            if numbers:
                entities['numbers'] = [int(n) for n in numbers]
            
            # Extract time-related units
            time_patterns = {
                'minute': ['minute', 'minit', 'منٹ', 'min'],
                'hour': ['hour', 'ghanta', 'ghante', 'گھنٹے', 'گھنٹہ'],
                'second': ['second', 'سیکنڈ', 'sec'],
                'day': ['day', 'din', 'دن'],
            }
            
            for unit, keywords in time_patterns.items():
                for keyword in keywords:
                    if keyword in text:
                        entities['time_unit'] = unit
                        break
                if 'time_unit' in entities:
                    break
            
            # Extract Pakistani cities
            city_patterns = {
                'karachi': ['karachi', 'کراچی', 'krachi'],
                'lahore': ['lahore', 'لاہور'],
                'islamabad': ['islamabad', 'اسلام آباد', 'isb'],
                'peshawar': ['peshawar', 'پشاور'],
                'quetta': ['quetta', 'کوئٹہ'],
                'multan': ['multan', 'ملتان'],
                'faisalabad': ['faisalabad', 'فیصل آباد'],
                'rawalpindi': ['rawalpindi', 'راولپنڈی', 'pindi']
            }
            
            for city, keywords in city_patterns.items():
                for keyword in keywords:
                    if keyword in text:
                        entities['city'] = city
                        break
                if 'city' in entities:
                    break
            
            # Extract prayer names
            prayer_patterns = {
                'fajr': ['fajr', 'فجر'],
                'zuhr': ['zuhr', 'zohr', 'ظہر'],
                'asr': ['asr', 'عصر'],
                'maghrib': ['maghrib', 'مغرب'],
                'isha': ['isha', 'عشاء', 'esha']
            }
            
            for prayer, keywords in prayer_patterns.items():
                for keyword in keywords:
                    if keyword in text:
                        entities['prayer_name'] = prayer
                        break
                if 'prayer_name' in entities:
                    break
            
            logger.debug(f"📦 Extracted entities: {entities}")
            
        except Exception as e:
            logger.error(f"❌ Entity extraction failed: {e}")
        
        return entities
    
    def get_all_intents(self) -> List[str]:
        """
        Get list of all supported intents
        
        Returns:
            List of intent names
        
        Example:
            >>> detector.get_all_intents()
            ['greeting', 'farewell', 'weather', 'time', ...]
        """
        return list(self.patterns.keys())
    
    def add_pattern(self, intent: str, keywords: List[str], confidence: float = 0.8):
        """
        Add new intent pattern dynamically (for extensibility)
        
        Args:
            intent: Intent name
            keywords: List of keywords for this intent
            confidence: Base confidence score (0.0 to 1.0)
        
        Example:
            >>> detector.add_pattern('music', ['song', 'گانا', 'music'], 0.85)
        """
        self.patterns[intent] = {
            'keywords': keywords,
            'confidence': confidence
        }
        logger.info(f"✅ Added new pattern for intent: {intent}")
    
    def remove_pattern(self, intent: str) -> bool:
        """
        Remove an intent pattern
        
        Args:
            intent: Intent name to remove
        
        Returns:
            True if removed, False if not found
        """
        if intent in self.patterns:
            del self.patterns[intent]
            logger.info(f"✅ Removed pattern for intent: {intent}")
            return True
        else:
            logger.warning(f"⚠️ Intent '{intent}' not found")
            return False


# Test the detector
if __name__ == "__main__":
    print("🧪 Testing IntentDetector...\n")
    
    detector = IntentDetector()
    
    # Test cases
    test_cases = [
        "السلام علیکم",
        "موسم کیسا ہے؟",
        "وقت کیا ہوا ہے؟",
        "کوئی لطیفہ سناؤ",
        "اللہ حافظ",
        "Hello, how are you?",
        "What's the weather like?",
        "Tell me a joke",
        "some random gibberish text xyz123"
    ]
    
    print("Testing intent detection:\n")
    for i, text in enumerate(test_cases, 1):
        intent, confidence, entities = detector.detect_intent(text)
        print(f"{i}. Text: '{text}'")
        print(f"   Intent: {intent} (confidence: {confidence:.2f})")
        print(f"   Entities: {entities}")
        print()
    
    print(f"\n✅ Supported intents: {detector.get_all_intents()}")
