from supabase import create_client, Client
from backend.core.config import settings, logger

class DatabaseManager:
    """
    Singleton class to manage Supabase database connections.
    Ensures only one instance of the client is created and shared across the app.
    """
    _instance: Client = None

    @classmethod
    def get_client(cls) -> Client:
        if cls._instance is None:
            try:
                logger.info("Initializing Supabase client connection...")
                cls._instance = create_client(
                    supabase_url=settings.SUPABASE_URL,
                    supabase_key=settings.SUPABASE_KEY
                )
                logger.info("Supabase client initialized successfully.")
            except Exception as e:
                logger.error(f"Failed to initialize Supabase client: {str(e)}")
                raise ConnectionError(f"Database connection failed: {str(e)}")
        
        return cls._instance

# Export a dependency-injectable callable for FastAPI
def get_db() -> Client:
    return DatabaseManager.get_client()