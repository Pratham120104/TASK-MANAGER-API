from pydantic import BaseModel
from typing import Optional

# Request schema for creating a task


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Request schema for updating a task


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Response schema for returning task info


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True
