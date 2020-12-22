from typing import List, Optional
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: int
    login: str
    name: str
    last_name: str

    class Config:
        orm_mode = True


UserSchema.update_forward_refs()
