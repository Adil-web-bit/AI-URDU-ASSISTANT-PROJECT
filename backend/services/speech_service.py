"""
Speech Service - Text-to-Speech using Google TTS
Converts Urdu/English text to audio files
"""
from gtts import gTTS
import os
from datetime import datetime
from pathlib import Path
from typing import Optional
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import AUDIO_OUTPUT_DIR, AUDIO_FORMAT, DEFAULT_LANGUAGE
from utils.logger import setup_logger
from utils.helpers import cleanup_old_files

logger = setup_logger(__name__)


class SpeechService:
    """
    Service for converting text to speech using Google TTS
    Completely FREE - no API keys required!
    """
    
    def __init__(self):
        """Initialize speech service"""
        self.output_dir = AUDIO_OUTPUT_DIR
        self.output_dir.mkdir(exist_ok=True)
        logger.info(f"✅ SpeechService initialized. Output directory: {self.output_dir}")
    
    def text_to_speech(self, text: str, lang: str = None) -> str:
        """
        Convert text to speech and save as MP3 file
        
        Args:
            text: Text to convert (Urdu or English)
            lang: Language code ('ur' for Urdu, 'en' for English)
                  If None, uses DEFAULT_LANGUAGE from config
        
        Returns:
            filename: Name of generated audio file (not full path)
        
        Raises:
            Exception: If speech generation fails
        
        Example:
            >>> service = SpeechService()
            >>> filename = service.text_to_speech("السلام علیکم", "ur")
            >>> print(filename)
            'speech_20251025_143022_123456.mp3'
        """
        try:
            # Use default language if not specified
            if lang is None:
                lang = DEFAULT_LANGUAGE
            
            # Validate language
            if lang not in ['ur', 'en']:
                logger.warning(f"Invalid language '{lang}', using 'ur'")
                lang = 'ur'
            
            # Generate unique filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = f"speech_{timestamp}.{AUDIO_FORMAT}"
            filepath = self.output_dir / filename
            
            logger.info(f"🎤 Generating speech: lang={lang}, text_length={len(text)}")
            logger.debug(f"Text preview: {text[:50]}...")
            
            # Create speech using gTTS
            # slow=False means normal speed (natural)
            tts = gTTS(text=text, lang=lang, slow=False)
            
            # Save to file
            tts.save(str(filepath))
            
            logger.info(f"✅ Speech generated successfully: {filename}")
            
            # Cleanup old files to save space
            self.cleanup_old_files()
            
            return filename
            
        except Exception as e:
            logger.error(f"❌ Speech generation failed: {str(e)}")
            raise Exception(f"Failed to generate speech: {str(e)}")
    
    def cleanup_old_files(self, max_files: int = 100):
        """
        Delete old audio files if count exceeds max_files
        Keeps the most recent files based on creation time
        
        Args:
            max_files: Maximum number of audio files to keep
        """
        try:
            cleanup_old_files(
                directory=self.output_dir,
                max_files=max_files,
                extension=f".{AUDIO_FORMAT}"
            )
            logger.debug(f"🧹 Cleanup completed. Max files: {max_files}")
        except Exception as e:
            logger.error(f"❌ Cleanup failed: {str(e)}")
    
    def get_audio_path(self, filename: str) -> Path:
        """
        Get full path to audio file
        
        Args:
            filename: Audio file name
        
        Returns:
            Full path to audio file
        
        Example:
            >>> service.get_audio_path("speech_123.mp3")
            Path('f:/urdu-voice-assistant/backend/audio_outputs/speech_123.mp3')
        """
        return self.output_dir / filename
    
    def file_exists(self, filename: str) -> bool:
        """
        Check if audio file exists
        
        Args:
            filename: Audio file name
        
        Returns:
            True if file exists, False otherwise
        
        Example:
            >>> service.file_exists("speech_123.mp3")
            True
        """
        filepath = self.get_audio_path(filename)
        exists = filepath.exists()
        logger.debug(f"File exists check: {filename} -> {exists}")
        return exists
    
    def get_audio_url(self, filename: str, base_url: str = "/api/v1/audio") -> str:
        """
        Get URL for accessing audio file
        
        Args:
            filename: Audio file name
            base_url: Base URL for audio endpoint
        
        Returns:
            URL string for audio file
        
        Example:
            >>> service.get_audio_url("speech_123.mp3")
            '/api/v1/audio/speech_123.mp3'
        """
        return f"{base_url}/{filename}"


# Test the service
if __name__ == "__main__":
    print("🧪 Testing SpeechService...\n")
    
    try:
        service = SpeechService()
        
        # Test Urdu speech
        print("1. Testing Urdu speech generation...")
        urdu_file = service.text_to_speech("السلام علیکم! یہ ایک ٹیسٹ ہے۔", "ur")
        print(f"   ✅ Urdu audio: {urdu_file}")
        
        # Test English speech
        print("\n2. Testing English speech generation...")
        english_file = service.text_to_speech("Hello! This is a test.", "en")
        print(f"   ✅ English audio: {english_file}")
        
        # Test file exists
        print("\n3. Testing file_exists...")
        exists = service.file_exists(urdu_file)
        print(f"   ✅ File exists: {exists}")
        
        # Test get_audio_path
        print("\n4. Testing get_audio_path...")
        path = service.get_audio_path(urdu_file)
        print(f"   ✅ Full path: {path}")
        
        print("\n✅ All SpeechService tests passed!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
