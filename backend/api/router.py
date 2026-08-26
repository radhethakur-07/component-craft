from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from supabase import Client
from typing import Optional, Dict, Any

from backend.db.supabase import get_db
from backend.services.ai_service import ai_service, AIProcessingError
from backend.core.config import logger

# Initialize APIRouter
router = APIRouter()

# --- Pydantic Schemas for Validation ---
class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=5, description="The user's description of the UI component")
    user_id: Optional[str] = Field(None, description="Optional UUID of the logged-in user")

class GenerateResponse(BaseModel):
    success: bool
    component_id: Optional[str]
    code: str
    message: str

# --- Endpoints ---
@router.post("/generate", response_model=GenerateResponse, status_code=201)
async def generate_component(request: GenerateRequest, db: Client = Depends(get_db)):
    """
    Endpoint to generate a React component from a text prompt.
    Validates input, calls AI service, and persists the result to Supabase.
    """
    try:
        # 1. Generate Code via AI Service
        logger.info(f"Processing generation request for prompt length: {len(request.prompt)}")
        react_code = ai_service.generate_ui_component(request.prompt)
        
        # 2. Prepare Database Payload
        payload: Dict[str, Any] = {
            "prompt": request.prompt,
            "react_code": react_code,
            "is_public": True
        }
        if request.user_id:
            payload["user_id"] = request.user_id
            
        # 3. Persist to Supabase
        db_response = db.table("components").insert(payload).execute()
        
        component_id = db_response.data[0]["id"] if db_response.data else None
        
        return GenerateResponse(
            success=True,
            component_id=str(component_id),
            code=react_code,
            message="Component generated and saved successfully."
        )
        
    except AIProcessingError as e:
        logger.error(f"AI Service Failure: {str(e)}")
        raise HTTPException(status_code=502, detail=f"AI Engine Error: {str(e)}")
    except Exception as e:
        logger.error(f"Internal Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred while processing the request.")