from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    TITLE: str
    VERSION: str
    SUMMARY: str
    DESCRIPTION: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"
