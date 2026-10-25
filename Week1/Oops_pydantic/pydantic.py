from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=18, le=120)


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    # Demonstration only: production mein database use hoga.
    saved_user = {
        "id": 1,
        "name": user.name.strip(),
        "email": str(user.email).lower(),
        "age": user.age,
    }

    return saved_user