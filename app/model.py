from pydantic import BaseModel, Field


class Create_user(BaseModel):
    name: str = Field(..., description="user name")
    email: str = Field(..., description="user email")
