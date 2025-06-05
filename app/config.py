from pydantic_settings import BaseSettings  # Import BaseSettings for config management

class Settings(BaseSettings):
    enable_telegram: bool = False  # Enable Telegram notifications
    telegram_token: str = ""       # Telegram bot token from .env
    chat_id: str = ""              # Telegram chat ID from .env

    class Config:
        env_file = ".env"  # Explicitly specify the .env file

settings = Settings()  # Create a settings instance for use in your app