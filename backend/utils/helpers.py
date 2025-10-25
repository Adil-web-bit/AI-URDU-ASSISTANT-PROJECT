"""
Helper utility functions for Urdu Voice Assistant
Includes text processing, language detection, file management, and date/time in Urdu
"""

import re
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


def clean_text(text: str) -> str:
    """
    Clean and normalize text by removing extra whitespace
    Preserves Urdu characters (Unicode range U+0600 to U+06FF)
    
    Args:
        text: Input text string
        
    Returns:
        Cleaned text string
    """
    if not text:
        return ""
    
    # Remove extra whitespace (replace multiple spaces with single space)
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def is_urdu_text(text: str) -> bool:
    """
    Check if text contains Urdu characters
    Urdu Unicode range: U+0600 to U+06FF (Arabic/Urdu script)
    
    Args:
        text: Input text string
        
    Returns:
        True if text contains Urdu characters, False otherwise
    """
    if not text:
        return False
    
    # Check for Urdu/Arabic Unicode characters
    urdu_pattern = re.compile(r'[\u0600-\u06FF]')
    return bool(urdu_pattern.search(text))


def detect_language(text: str) -> str:
    """
    Detect the primary language of the text
    
    Args:
        text: Input text string
        
    Returns:
        Language code: "ur" (Urdu), "en" (English), or "mixed"
    """
    if not text:
        return "en"
    
    # Count Urdu characters
    urdu_chars = len(re.findall(r'[\u0600-\u06FF]', text))
    
    # Count English characters
    english_chars = len(re.findall(r'[a-zA-Z]', text))
    
    # Determine language based on character count
    if urdu_chars > 0 and english_chars > 0:
        # Both languages present
        if urdu_chars > english_chars:
            return "ur"
        elif english_chars > urdu_chars:
            return "mixed"
        else:
            return "mixed"
    elif urdu_chars > 0:
        return "ur"
    elif english_chars > 0:
        return "en"
    else:
        return "en"  # Default to English


def cleanup_old_files(directory: Path, max_files: int = 50, extension: str = ".mp3") -> None:
    """
    Clean up old files in a directory to maintain a maximum number of files
    Deletes oldest files first based on creation time
    
    Args:
        directory: Path to directory to clean
        max_files: Maximum number of files to keep
        extension: File extension to filter by
    """
    try:
        if not directory.exists():
            return
        
        # Get all files with specified extension
        files = list(directory.glob(f"*{extension}"))
        
        if len(files) <= max_files:
            return  # No cleanup needed
        
        # Sort files by creation time (oldest first)
        files.sort(key=lambda f: f.stat().st_ctime)
        
        # Calculate how many files to delete
        files_to_delete = len(files) - max_files
        
        # Delete oldest files
        for file in files[:files_to_delete]:
            try:
                file.unlink()
                logger.info(f"Deleted old file: {file.name}")
            except Exception as e:
                logger.error(f"Failed to delete file {file.name}: {e}")
                
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")


def get_current_time_urdu() -> str:
    """
    Get current time formatted in Urdu
    
    Returns:
        Time string in Urdu format (e.g., "ابھی 3:45 دوپہر بجے ہیں")
    """
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    
    # Convert to 12-hour format
    hour_12 = hour % 12
    if hour_12 == 0:
        hour_12 = 12
    
    # Determine period (صبح، دوپہر، شام، رات)
    if 5 <= hour < 12:
        period = "صبح"  # Morning
    elif 12 <= hour < 17:
        period = "دوپہر"  # Afternoon
    elif 17 <= hour < 21:
        period = "شام"  # Evening
    else:
        period = "رات"  # Night
    
    return f"ابھی {hour_12}:{minute:02d} {period} بجے ہیں"


def get_current_date_urdu() -> str:
    """
    Get current date formatted in Urdu
    
    Returns:
        Date string in Urdu format (e.g., "آج پیر، 24 اکتوبر 2025 ہے")
    """
    now = datetime.now()
    
    # Urdu day names (Monday to Sunday)
    urdu_days = ["پیر", "منگل", "بدھ", "جمعرات", "جمعہ", "ہفتہ", "اتوار"]
    
    # Urdu month names
    urdu_months = [
        "جنوری", "فروری", "مارچ", "اپریل", "مئی", "جون",
        "جولائی", "اگست", "ستمبر", "اکتوبر", "نومبر", "دسمبر"
    ]
    
    day_name = urdu_days[now.weekday()]
    month_name = urdu_months[now.month - 1]
    
    return f"آج {day_name}، {now.day} {month_name} {now.year} ہے"


def load_json_file(filepath: Path) -> Dict[str, Any]:
    """
    Load JSON file with UTF-8 encoding
    
    Args:
        filepath: Path to JSON file
        
    Returns:
        Dictionary containing JSON data, or empty dict on failure
    """
    try:
        if not filepath.exists():
            logger.warning(f"JSON file not found: {filepath}")
            return {}
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info(f"✅ Loaded JSON file: {filepath.name}")
            return data
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {filepath}: {e}")
        return {}
    except Exception as e:
        logger.error(f"Error loading JSON file {filepath}: {e}")
        return {}


def save_json_file(filepath: Path, data: Dict[str, Any]) -> bool:
    """
    Save dictionary to JSON file with UTF-8 encoding
    
    Args:
        filepath: Path to save JSON file
        data: Dictionary to save
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Create parent directory if it doesn't exist
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        logger.info(f"✅ Saved JSON file: {filepath.name}")
        return True
        
    except Exception as e:
        logger.error(f"Error saving JSON file {filepath}: {e}")
        return False


def format_urdu_number(number: int) -> str:
    """
    Convert number to Urdu text (basic implementation)
    
    Args:
        number: Integer number
        
    Returns:
        Number in Urdu text
    """
    urdu_digits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
    return ''.join(urdu_digits[int(d)] for d in str(number))


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to maximum length
    
    Args:
        text: Input text
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


# Example usage and testing
if __name__ == "__main__":
    print("🧪 Testing Helper Functions...\n")
    
    # Test clean_text
    print("1. clean_text:")
    print(f"   {clean_text('  السلام    علیکم   ')}")
    
    # Test is_urdu_text
    print("\n2. is_urdu_text:")
    print(f"   'سلام' -> {is_urdu_text('سلام')}")
    print(f"   'Hello' -> {is_urdu_text('Hello')}")
    
    # Test detect_language
    print("\n3. detect_language:")
    print(f"   'سلام' -> {detect_language('سلام')}")
    print(f"   'Hello' -> {detect_language('Hello')}")
    print(f"   'Hello سلام' -> {detect_language('Hello سلام')}")
    
    # Test get_current_time_urdu
    print("\n4. get_current_time_urdu:")
    print(f"   {get_current_time_urdu()}")
    
    # Test get_current_date_urdu
    print("\n5. get_current_date_urdu:")
    print(f"   {get_current_date_urdu()}")
    
    print("\n✅ All helper functions tested!")
