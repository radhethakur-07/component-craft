import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.core.config import settings, logger
from backend.api.router import router as api_router

# Initialize the FastAPI App with metadata for Auto-Docs (Swagger UI)
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-powered Text-to-React UI Builder API",
    version="1.0.0",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
)

# CORS Middleware Setup (Production Ready)
# allow_origins=["*"] allows requests from anywhere (like your Vercel app).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

# Include API Routers
app.include_router(api_router, prefix=settings.API_V1_STR, tags=["Generation"])

# Global Exception Handler (Pro feature)
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.critical(f"Unhandled exception on {request.url.path}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"success": False, "message": "An internal system error occurred. Engineers have been notified."}
    )

# System Healthcheck Endpoint
@app.get("/health", tags=["System"])
async def health_check():
    """Returns the system status, useful for uptime monitoring and Load Balancers."""
    # Production ke hisaab se dynamic environment detect karega
    env = os.getenv("ENVIRONMENT", "production")
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "environment": env
    }