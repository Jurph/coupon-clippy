"""Configuration settings for the application."""
import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file (secrets)
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Load configuration from .config file (non-secrets)
config_path = Path(__file__).parent.parent.parent / '.config'
if config_path.exists():
    load_dotenv(dotenv_path=config_path)

class Settings:
    """Application settings loaded from environment variables and config."""
    
    # API Keys (from .env)
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    ANTHROPIC_API_KEY: Optional[str] = os.getenv('ANTHROPIC_API_KEY')
    GOOGLE_API_KEY: Optional[str] = os.getenv('GOOGLE_API_KEY')
    OLLAMA_API_KEY: Optional[str] = os.getenv('OLLAMA_API_KEY')
    
    # Database (from .env)
    DATABASE_URL: Optional[str] = os.getenv('DATABASE_URL')
    
    # Store API Keys (from .env)
    GIANT_API_KEY: Optional[str] = os.getenv('GIANT_API_KEY')
    WEGMANS_API_KEY: Optional[str] = os.getenv('WEGMANS_API_KEY')
    SAFEWAY_API_KEY: Optional[str] = os.getenv('SAFEWAY_API_KEY')
    
    # Application Settings (from .config)
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')
    DEBUG: bool = os.getenv('DEBUG', 'true').lower() == 'true'
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    
    # Model Configuration (from .config)
    DEFAULT_MODEL: str = os.getenv('DEFAULT_MODEL', 'gpt-3.5-turbo')
    TEMPERATURE: float = float(os.getenv('TEMPERATURE', '0.0'))
    MAX_TOKENS: int = int(os.getenv('MAX_TOKENS', '2000'))
    
    # Web Scraping (from .config)
    SCRAPING_DELAY: float = float(os.getenv('SCRAPING_DELAY', '1.0'))
    USER_AGENT: str = os.getenv('USER_AGENT', '')
    
    # Cache Configuration (from .config)
    CACHE_DIR: str = os.getenv('CACHE_DIR', './cache')
    CACHE_TTL: int = int(os.getenv('CACHE_TTL', '3600'))
    
    # Security (from .config)
    API_RATE_LIMIT: int = int(os.getenv('API_RATE_LIMIT', '100'))
    ALLOWED_ORIGINS: list[str] = os.getenv('ALLOWED_ORIGINS', '').split(',')
    
    @classmethod
    def validate(cls) -> None:
        """Validate that required settings are present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY environment variable is not set. "
                "Please create a .env file with your API key."
            )
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if running in development environment."""
        return cls.ENVIRONMENT.lower() == 'development'

# Create settings instance
settings = Settings()

# Validate settings on import
settings.validate() 