from pydantic.v1 import BaseSettings
class Settings(BaseSettings):
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    CATALOG: str
    SHEMA: str

    class Config:
        env_file = ".env"