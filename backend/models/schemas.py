"""
Pydantic models for request/response validation
Defines data schemas for the Urdu Voice Assistant API
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
from datetime import datetime


class CommandRequest(BaseModel):
    """Request model for voice command processing"""
    
    text: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Voice command text in Urdu or English"
    )
    user_id: Optional[str] = Field(
        None,
        description="Optional user identifier for tracking"
    )
    language: Optional[str] = Field(
        "auto",
        description="Language code: 'ur', 'en', or 'auto' for auto-detection"
    )
    
    @validator('text')
    def validate_text(cls, v):
        """Validate and clean text input"""
        if not v or not v.strip():
            raise ValueError("Text cannot be empty")
        return v.strip()
    
    class Config:
        schema_extra = {
            "example": {
                "text": "السلام علیکم، وقت کیا ہوا ہے؟",
                "user_id": "user_123",
                "language": "auto"
            }
        }


class IntentResult(BaseModel):
    """Model for intent detection results"""
    
    intent: str = Field(
        ...,
        description="Detected intent category"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1"
    )
    entities: Dict[str, Any] = Field(
        default_factory=dict,
        description="Extracted entities from the command"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "intent": "greeting",
                "confidence": 0.95,
                "entities": {}
            }
        }


class CommandResponse(BaseModel):
    """Response model for processed voice commands"""
    
    response_text: str = Field(
        ...,
        description="Generated response text in Urdu"
    )
    audio_file: Optional[str] = Field(
        None,
        description="URL or path to generated audio file"
    )
    intent: str = Field(
        ...,
        description="Detected intent of the command"
    )
    confidence: float = Field(
        ...,
        description="Confidence score of intent detection"
    )
    language: str = Field(
        ...,
        description="Detected language of input"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Response generation timestamp"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "response_text": "السلام علیکم! کیا حال ہے؟",
                "audio_file": "/api/v1/audio/response_123.mp3",
                "intent": "greeting",
                "confidence": 0.95,
                "language": "ur",
                "timestamp": "2025-10-24T12:30:00"
            }
        }


class HealthResponse(BaseModel):
    """Health check response model"""
    
    status: str = Field(
        default="healthy",
        description="Service health status"
    )
    version: str = Field(
        default="1.0.0",
        description="API version"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Health check timestamp"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "status": "healthy",
                "version": "1.0.0",
                "timestamp": "2025-10-24T12:30:00"
            }
        }


class CommandInfo(BaseModel):
    """Model for command information"""
    
    category: str = Field(
        ...,
        description="Command category"
    )
    examples: List[str] = Field(
        ...,
        description="Example commands in Urdu"
    )
    description: str = Field(
        ...,
        description="Description of the command in Urdu"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "category": "greeting",
                "examples": ["سلام", "ہیلو", "آداب"],
                "description": "اردو وائس اسسٹنٹ سے بات شروع کریں"
            }
        }


class CommandsListResponse(BaseModel):
    """Response model for available commands list"""
    
    commands: List[CommandInfo] = Field(
        ...,
        description="List of available commands"
    )
    total: int = Field(
        ...,
        description="Total number of commands"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "commands": [
                    {
                        "category": "greeting",
                        "examples": ["سلام", "ہیلو"],
                        "description": "بات شروع کریں"
                    }
                ],
                "total": 8
            }
        }


class ErrorResponse(BaseModel):
    """Error response model"""
    
    error: str = Field(
        ...,
        description="Error message"
    )
    detail: Optional[str] = Field(
        None,
        description="Detailed error information"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Error timestamp"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "error": "Invalid request",
                "detail": "Text field is required",
                "timestamp": "2025-10-24T12:30:00"
            }
        }


class AudioGenerationRequest(BaseModel):
    """Request model for audio generation"""
    
    text: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Text to convert to speech"
    )
    language: str = Field(
        default="ur",
        description="Language code for speech synthesis"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "text": "السلام علیکم! کیسے ہیں آپ؟",
                "language": "ur"
            }
        }


class ConversationHistoryItem(BaseModel):
    """Model for conversation history item"""
    
    user_input: str = Field(
        ...,
        description="User's input text"
    )
    assistant_response: str = Field(
        ...,
        description="Assistant's response text"
    )
    intent: str = Field(
        ...,
        description="Detected intent"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Conversation timestamp"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "user_input": "وقت کیا ہوا ہے؟",
                "assistant_response": "ابھی 3:45 دوپہر بجے ہیں",
                "intent": "time",
                "timestamp": "2025-10-24T15:45:00"
            }
        }


# Example usage and validation testing
if __name__ == "__main__":
    print("🧪 Testing Pydantic Models...\n")
    
    # Test CommandRequest
    print("1. CommandRequest:")
    request = CommandRequest(
        text="السلام علیکم",
        user_id="user_123",
        language="ur"
    )
    print(f"   ✅ {request.json(ensure_ascii=False, indent=2)}")
    
    # Test IntentResult
    print("\n2. IntentResult:")
    intent = IntentResult(
        intent="greeting",
        confidence=0.95,
        entities={"greeting_type": "formal"}
    )
    print(f"   ✅ {intent.json(indent=2)}")
    
    # Test CommandResponse
    print("\n3. CommandResponse:")
    response = CommandResponse(
        response_text="السلام علیکم! کیا حال ہے؟",
        audio_file="/audio/response_123.mp3",
        intent="greeting",
        confidence=0.95,
        language="ur"
    )
    print(f"   ✅ {response.json(ensure_ascii=False, indent=2)}")
    
    print("\n✅ All Pydantic models validated successfully!")
