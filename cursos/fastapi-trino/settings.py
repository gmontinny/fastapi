from pydantic import Field
from pydantic.v1 import BaseSettings
class Settings(BaseSettings):
    HOST: str = Field(..., env="HOST")
    PORT: int = Field(..., env="PORT")
    USER: str = Field(..., env="USER")
    PASSWORD: str = Field(..., env="PASSWORD")
    CATALOG: str = Field(..., env="CATALOG")
    SCHEMA: str = Field(..., env="SCHEMA")
