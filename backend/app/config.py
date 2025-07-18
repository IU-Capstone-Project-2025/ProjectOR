from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    JWT_SECRET_KEY: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
