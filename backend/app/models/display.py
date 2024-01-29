from pydantic import BaseModel, validator
from uuid import UUID
from typing import Optional
from enum import Enum


class DisplayStatusEnum(str, Enum):
    active = 'active'
    disabled = 'disabled'
    pending = 'pending'

class Display(BaseModel):
    id: Optional[UUID] = None
    name: str 
    description: str
    web_app: str 
    status: DisplayStatusEnum = DisplayStatusEnum.disabled
    api_key: Optional[str] = ""
    challenge_code: Optional[str] = None


    @validator('name', 'description', 'web_app')
    def string_must_not_be_empty(cls, val):
        if not val or not val.strip():
            raise ValueError('Field must not be empty')
        return val