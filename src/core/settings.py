from pydantic_settings import BaseSettings, SettingsConfigDict
from utils.logger import logger
from typing import Optional


class Settings(BaseSettings):
    # Server configuration
    SERVER_NAME: str = "MCP Server"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    TRANSPORT: str = "http"

    # Other environment variables
    INTERNAL_API_URL: Optional[str] = "http://localhost:9000/api"

    # Dynamically warn about unset variables
    def __init__(self, **kwargs):
        # Initialize the settings first
        super().__init__(**kwargs)

        # Dynamically check all attributes that are None
        for field, value in self.__dict__.items():
            if value is None:
                logger.warning(f"{field} is not set. This might cause issues.")

    # Pydantic settings configuration
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
