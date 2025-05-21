import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Alternativa para rodar localmente, caso não existir .env, considera variável de ambiente 
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str # Precisa conter o mesmo nome da variável de ambiente