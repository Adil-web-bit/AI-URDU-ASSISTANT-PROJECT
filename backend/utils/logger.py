"""
Logging utility for Urdu Voice Assistant
Provides configured logger with file and console handlers
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

# Import config
import os
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import LOG_DIR, LOG_LEVEL, LOG_FORMAT, LOG_DATE_FORMAT


def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """
    Set up and configure logger with console and file handlers
    
    Args:
        name: Logger name (usually __name__ from calling module)
        log_file: Optional custom log file name
        
    Returns:
        Configured logger instance
    """
    
    # Create logger
    logger = logging.getLogger(name)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    # Set logging level
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    # Create formatter with UTF-8 support for Urdu text
    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT
    )
    
    # Console Handler (outputs to terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    
    # Ensure console supports UTF-8 encoding
    if hasattr(console_handler.stream, 'reconfigure'):
        console_handler.stream.reconfigure(encoding='utf-8')
    
    logger.addHandler(console_handler)
    
    # File Handler (saves to log file)
    try:
        # Create log filename with date
        if log_file is None:
            log_filename = f"assistant_{datetime.now().strftime('%Y%m%d')}.log"
        else:
            log_filename = log_file
            
        log_filepath = LOG_DIR / log_filename
        
        # Create file handler with UTF-8 encoding
        file_handler = logging.FileHandler(
            log_filepath,
            encoding='utf-8',
            mode='a'  # Append mode
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        
    except Exception as e:
        logger.error(f"Failed to create file handler: {e}")
    
    # Prevent propagation to root logger
    logger.propagate = False
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get or create a logger instance
    
    Args:
        name: Logger name
        
    Returns:
        Logger instance
    """
    return setup_logger(name)


# Example usage
if __name__ == "__main__":
    # Test logger
    test_logger = setup_logger("test_logger")
    test_logger.info("✅ Logger initialized successfully!")
    test_logger.debug("🔍 Debug message test")
    test_logger.info("ℹ️ Info message test")
    test_logger.warning("⚠️ Warning message test")
    test_logger.error("❌ Error message test")
    test_logger.info("🇵🇰 اردو ٹیکسٹ ٹیسٹ - Urdu text support working!")
