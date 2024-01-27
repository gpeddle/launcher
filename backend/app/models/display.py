from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class Display(BaseModel):
    id: UUID = None
    name: str
    description: str
    web_app: str
    status: str
    api_key: str
    challenge_code: Optional[str] = None
