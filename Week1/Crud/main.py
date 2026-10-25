
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="User Management API")

# Temporary in-memory storage for practice
users = {
    1: {"id": 1, "name": "Aman", "email": "aman@example.com"},
    2: {"id": 2, "name": "Riya", "email": "riya@example.com"},
}
next_user_id = 3


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: str | None = None


@app.get("/")
def home():
    return {"message": "User API is running"}


# READ: Get all users
@app.get("/users")
def get_users():
    return list(users.values())


# READ: Get one user
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# CREATE: Add a user
@app.post("/users")
def create_user(data: UserCreate):
    global next_user_id

    for user in users.values():
        if user["email"] == data.email:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

    user = {
        "id": next_user_id,
        **data.model_dump()
    }

    users[next_user_id] = user
    next_user_id += 1

    return user


# UPDATE: Replace the entire user
@app.put("/users/{user_id}")
def replace_user(user_id: int, data: UserCreate):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = {
        "id": user_id,
        **data.model_dump()
    }

    return users[user_id]


# UPDATE: Change selected fields
@app.patch("/users/{user_id}")
def update_user(user_id: int, data: UserUpdate):
    user = users.get(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    changes = data.model_dump(exclude_unset=True)

    for field, value in changes.items():
        if value is None:
            raise HTTPException(
                status_code=422,
                detail=f"{field} cannot be null"
            )

    user.update(changes)
    return user


# DELETE: Remove a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    del users[user_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
