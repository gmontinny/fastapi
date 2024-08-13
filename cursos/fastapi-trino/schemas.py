from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field, validator


class TrilhaBase(BaseModel):
    situacao: str
    email: str
    sub_orgao: Optional[int] = Field(None, nullable=True)
    nm_orgao: str
    origem: str
    dtca: Optional[datetime] = Field(..., strict=True)
    dtde: Optional[datetime] = Field(None, nullable=True)
    hash: str

    @validator("dtca", pre=True)
    def string_to_date(cls, value):
        date_format = '%d/%m/%Y'
        return date.strptime(value, date_format) if isinstance(value, str) else value


class TrilhaRequest(TrilhaBase):
    ...

class TrilhaResponse(TrilhaBase):
    id: str

    class Config:
        orm_mode = True
        from_attributes = True