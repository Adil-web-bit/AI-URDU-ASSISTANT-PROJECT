"""
Main FastAPI Application for Urdu Voice Assistant
Production-ready REST API server with complete voice command processing
"""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from pathlib import Path
from datetime import datetime
import uvicorn

# Import configurations
from config import (
    PROJECT_NAME,
    API_VERSION,
    API_PREFIX,
    CORS_ORIGINS,
    HOST,
    PORT,
    RELOAD,
    AUDIO_OUTPUT_DIR,
    PROJECT_DESCRIPTION
)

# Import models
from models.schemas import (
    CommandRequest,
    CommandResponse,
    HealthResponse,
    CommandsListResponse,
    ErrorResponse
)

# Import services
from services.command_service import CommandService

# Import utilities
from utils.logger import setup_logger

# Setup logger
logger = setup_logger(__name__)

# Initialize command service globally
command_service = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for startup and shutdown
    Manages application lifecycle and resource initialization
    """
    # Startup
    logger.info("=" * 60)
    logger.info(f"🚀 Starting {PROJECT_NAME}")
    logger.info("=" * 60)
    
    global command_service
    try:
        logger.info("Initializing CommandService...")
        command_service = CommandService()
        logger.info("✅ CommandService initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize CommandService: {e}")
        raise
    
    logger.info(f"📡 API Version: {API_VERSION}")
    logger.info(f"🌐 Server: http://{HOST}:{PORT}")
    logger.info(f"📖 API Docs: http://{HOST}:{PORT}/docs")
    logger.info(f"📖 ReDoc: http://{HOST}:{PORT}/redoc")
    logger.info(f"🔊 Audio output: {AUDIO_OUTPUT_DIR}")
    logger.info(f"🎯 CORS origins: {', '.join(CORS_ORIGINS)}")
    logger.info("=" * 60)
    logger.info("✅ Server ready to accept requests!")
    logger.info("=" * 60)
    
    yield
    
    # Shutdown
    logger.info("=" * 60)
    logger.info("🛑 Shutting down Urdu Voice Assistant...")
    logger.info("👋 Goodbye!")
    logger.info("=" * 60)


# Create FastAPI app
app = FastAPI(
    title=PROJECT_NAME,
    description=PROJECT_DESCRIPTION,
    version=API_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{API_PREFIX}/openapi.json"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Mount static files for audio (accessible at /audio/)
app.mount("/audio", StaticFiles(directory=str(AUDIO_OUTPUT_DIR)), name="audio")

# ============================================================================
# API ROUTES
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint - API information and welcome message
    
    Returns:
        API metadata and useful links
    """
    return {
        "name": PROJECT_NAME,
        "version": API_VERSION,
        "status": "running",
        "message": "اردو وائس اسسٹنٹ - Urdu Voice Assistant API",
        "description": "AI-powered voice assistant for Urdu/English commands",
        "endpoints": {
            "docs": "/docs",
            "redoc": "/redoc",
            "health": "/health",
            "process_command": f"{API_PREFIX}/process-command",
            "commands": f"{API_PREFIX}/commands",
            "intents": f"{API_PREFIX}/intents"
        },
        "github": "https://github.com/your-repo",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Health check endpoint
    
    Returns:
        HealthResponse: Current health status of the API
    
    Example:
        GET /health
        
        Response:
        {
            "status": "healthy",
            "version": "1.0.0",
            "timestamp": "2025-10-25T00:00:00"
        }
    """
    try:
        return HealthResponse(
            status="healthy",
            version=API_VERSION,
            timestamp=datetime.now()
        )
    except Exception as e:
        logger.error(f"❌ Health check failed: {e}")
        raise HTTPException(status_code=500, detail="Service unhealthy")


@app.post(f"{API_PREFIX}/process-command", response_model=CommandResponse, tags=["Commands"])
async def process_command(request: CommandRequest):
    """
    Process user voice command and generate response
    
    This is the main endpoint for voice command processing.
    It detects intent, generates response, and creates audio.
    
    Args:
        request: CommandRequest with text, user_id, language
    
    Returns:
        CommandResponse: Response text, audio file, intent, confidence
    
    Raises:
        HTTPException: 400 for invalid input, 500 for processing errors
    
    Example:
        POST /api/v1/process-command
        Content-Type: application/json
        
        {
            "text": "السلام علیکم، کیا حال ہے؟",
            "user_id": "user_123",
            "language": "auto"
        }
        
        Response:
        {
            "response_text": "السلام علیکم! میں ٹھیک ہوں، شکریہ۔",
            "audio_file": "speech_20251025_120000_123456.mp3",
            "intent": "greeting",
            "confidence": 0.95,
            "language": "ur",
            "timestamp": "2025-10-25T12:00:00"
        }
    """
    try:
        logger.info(f"📥 Received command from user: {request.user_id or 'anonymous'}")
        logger.debug(f"Command text: '{request.text[:100]}...'")
        
        # Validate input
        if not request.text or len(request.text.strip()) == 0:
            logger.warning("⚠️ Empty text provided")
            raise HTTPException(
                status_code=400,
                detail="Text cannot be empty"
            )
        
        if len(request.text) > 500:
            logger.warning("⚠️ Text too long")
            raise HTTPException(
                status_code=400,
                detail="Text exceeds maximum length of 500 characters"
            )
        
        # Process command through CommandService
        result = await command_service.process_command(
            text=request.text,
            user_id=request.user_id,
            language_hint=request.language
        )
        
        # Create response object
        response = CommandResponse(
            response_text=result['response_text'],
            audio_file=result['audio_file'],
            intent=result['intent'],
            confidence=result['confidence'],
            language=result['language'],
            timestamp=datetime.now()
        )
        
        logger.info(f"✅ Command processed successfully: {result['intent']} (confidence: {result['confidence']})")
        
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Command processing failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process command: {str(e)}"
        )


@app.get(f"{API_PREFIX}/audio/{{filename}}", tags=["Audio"])
async def get_audio(filename: str):
    """
    Retrieve generated audio file
    
    Args:
        filename: Name of the audio file (e.g., speech_xxx.mp3)
    
    Returns:
        FileResponse: Audio file with MP3 content type
    
    Raises:
        HTTPException: 400 for invalid filename, 404 if not found
    
    Example:
        GET /api/v1/audio/speech_20251025_120000_123456.mp3
        
        Response: MP3 audio file
    """
    try:
        # Security: Validate filename (prevent path traversal attacks)
        if ".." in filename or "/" in filename or "\\" in filename:
            logger.warning(f"⚠️ Invalid filename attempt: {filename}")
            raise HTTPException(
                status_code=400,
                detail="Invalid filename format"
            )
        
        # Only allow .mp3 files
        if not filename.endswith('.mp3'):
            raise HTTPException(
                status_code=400,
                detail="Only MP3 files are supported"
            )
        
        # Check if file exists
        audio_path = AUDIO_OUTPUT_DIR / filename
        
        if not audio_path.exists():
            logger.warning(f"⚠️ Audio file not found: {filename}")
            raise HTTPException(
                status_code=404,
                detail=f"Audio file not found: {filename}"
            )
        
        logger.debug(f"📤 Serving audio file: {filename}")
        
        # Return audio file with proper headers
        return FileResponse(
            path=str(audio_path),
            media_type="audio/mpeg",
            filename=filename,
            headers={
                "Cache-Control": "public, max-age=3600",  # Cache for 1 hour
                "Accept-Ranges": "bytes"
            }
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Failed to serve audio: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve audio file"
        )


@app.get(f"{API_PREFIX}/commands", response_model=CommandsListResponse, tags=["Commands"])
async def get_commands():
    """
    Get list of available commands with examples
    
    Returns detailed information about all supported commands,
    including examples in Urdu and descriptions.
    
    Returns:
        CommandsListResponse: List of commands with examples
    
    Example:
        GET /api/v1/commands
        
        Response:
        {
            "commands": [
                {
                    "category": "greeting",
                    "examples": ["سلام", "ہیلو", "آداب", "السلام علیکم"],
                    "description": "اردو وائس اسسٹنٹ سے بات شروع کریں"
                },
                ...
            ],
            "total": 8
        }
    """
    try:
        from config import COMMANDS_FILE
        from utils.helpers import load_json_file
        from models.schemas import CommandInfo
        
        # Load commands from JSON file
        commands_data = load_json_file(COMMANDS_FILE)
        
        if not commands_data or 'commands' not in commands_data:
            logger.error("❌ Commands data not available")
            raise HTTPException(
                status_code=500,
                detail="Commands data not available"
            )
        
        # Parse commands into CommandInfo objects
        commands_list = [
            CommandInfo(**cmd) for cmd in commands_data['commands']
        ]
        
        logger.info(f"📋 Returning {len(commands_list)} available commands")
        
        return CommandsListResponse(
            commands=commands_list,
            total=len(commands_list)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Failed to get commands: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve commands"
        )


@app.get(f"{API_PREFIX}/intents", tags=["Commands"])
async def get_intents():
    """
    Get list of supported intent names
    
    Returns all intent categories that the system can detect.
    
    Returns:
        dict: List of intent names with metadata
    
    Example:
        GET /api/v1/intents
        
        Response:
        {
            "intents": ["greeting", "farewell", "weather", "time", ...],
            "total": 11,
            "message": "دستیاب intents کی فہرست"
        }
    """
    try:
        result = command_service.get_available_commands()
        
        return {
            "intents": result['intents'],
            "total": result['total'],
            "message": "دستیاب intents کی فہرست",
            "status": "success"
        }
        
    except Exception as e:
        logger.error(f"❌ Failed to get intents: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve intents"
        )


@app.post(f"{API_PREFIX}/test-speech", tags=["Testing"])
async def test_speech(
    text: str = Query(..., description="Text to convert to speech"),
    lang: str = Query("ur", description="Language code (ur or en)")
):
    """
    Test speech generation endpoint (for development/testing)
    
    Directly generates audio from text without intent detection.
    Useful for testing the speech synthesis service.
    
    Args:
        text: Text to convert to speech
        lang: Language code ('ur' for Urdu, 'en' for English)
    
    Returns:
        dict: Audio file information
    
    Example:
        POST /api/v1/test-speech?text=ہیلو دنیا&lang=ur
        
        Response:
        {
            "message": "Speech generated successfully",
            "audio_file": "speech_xxx.mp3",
            "text": "ہیلو دنیا",
            "language": "ur",
            "audio_url": "/api/v1/audio/speech_xxx.mp3"
        }
    """
    try:
        # Validate input
        if not text or len(text.strip()) == 0:
            raise HTTPException(
                status_code=400,
                detail="Text parameter cannot be empty"
            )
        
        if len(text) > 1000:
            raise HTTPException(
                status_code=400,
                detail="Text exceeds maximum length of 1000 characters"
            )
        
        if lang not in ['ur', 'en']:
            raise HTTPException(
                status_code=400,
                detail="Language must be 'ur' (Urdu) or 'en' (English)"
            )
        
        logger.info(f"🧪 Testing speech generation: lang={lang}, text_length={len(text)}")
        
        # Generate speech directly
        audio_filename = command_service.speech_service.text_to_speech(
            text=text,
            lang=lang
        )
        
        logger.info(f"✅ Test speech generated: {audio_filename}")
        
        return {
            "message": "Speech generated successfully",
            "audio_file": audio_filename,
            "text": text,
            "language": lang,
            "audio_url": f"{API_PREFIX}/audio/{audio_filename}",
            "timestamp": datetime.now().isoformat()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Speech test failed: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Speech generation failed: {str(e)}"
        )


@app.get(f"{API_PREFIX}/stats", tags=["Statistics"])
async def get_stats():
    """
    Get API statistics and metrics
    
    Returns information about audio files, supported features,
    and system status.
    
    Returns:
        dict: Statistics and metrics
    
    Example:
        GET /api/v1/stats
        
        Response:
        {
            "audio_files_generated": 42,
            "total_audio_size_mb": 12.5,
            "supported_languages": ["ur", "en"],
            "supported_intents": 11,
            "api_version": "1.0.0",
            "status": "operational"
        }
    """
    try:
        import os
        
        # Count audio files
        audio_files = list(AUDIO_OUTPUT_DIR.glob("*.mp3"))
        audio_count = len(audio_files)
        
        # Calculate total size
        total_size = sum(f.stat().st_size for f in audio_files if f.exists())
        total_size_mb = round(total_size / (1024 * 1024), 2)
        
        # Get service stats
        service_status = command_service.get_service_status()
        
        return {
            "audio_files_generated": audio_count,
            "total_audio_size_mb": total_size_mb,
            "supported_languages": ["ur", "en"],
            "supported_intents": len(command_service.intent_detector.get_all_intents()),
            "intents": command_service.intent_detector.get_all_intents(),
            "api_version": API_VERSION,
            "service_status": service_status,
            "status": "operational",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"❌ Failed to get stats: {e}")
        return {
            "error": "Failed to retrieve statistics",
            "status": "error",
            "detail": str(e)
        }


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(404)
async def not_found_handler(request, exc):
    """
    Custom 404 error handler
    
    Returns user-friendly error message for not found resources
    """
    logger.warning(f"⚠️ 404 Not Found: {request.url.path}")
    return JSONResponse(
        status_code=404,
        content={
            "error": "Not Found",
            "message": "The requested resource was not found",
            "path": str(request.url.path),
            "suggestion": "Check the API documentation at /docs",
            "timestamp": datetime.now().isoformat()
        }
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """
    Custom 500 error handler
    
    Returns generic error message without exposing internals
    """
    logger.error(f"❌ 500 Internal Server Error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred",
            "suggestion": "Please try again later or contact support",
            "timestamp": datetime.now().isoformat()
        }
    )


# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == "__main__":
    """
    Run the FastAPI server directly
    
    Usage:
        python main.py
    
    Server will start at http://0.0.0.0:8000
    API docs available at http://0.0.0.0:8000/docs
    """
    print("\n" + "=" * 60)
    print(f"🚀 {PROJECT_NAME}")
    print("=" * 60)
    print(f"📡 Host: {HOST}")
    print(f"🔌 Port: {PORT}")
    print(f"📖 Docs: http://{HOST}:{PORT}/docs")
    print(f"📖 ReDoc: http://{HOST}:{PORT}/redoc")
    print(f"🔄 Auto-reload: {RELOAD}")
    print("=" * 60)
    print("Press CTRL+C to stop the server")
    print("=" * 60 + "\n")
    
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=RELOAD,
        log_level="info"
    )
