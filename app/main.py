from fastapi import FastAPI, Query, status, HTTPException
from app.model import Create_user
import random

app = FastAPI(title="Uptime University")

temp_memory = []
id_ref = []


@app.get("/", status_code=status.HTTP_200_OK)
async def welcome():
    return {"message": "Welcome to the Uptime University!"}


@app.get("/users", status_code=status.HTTP_200_OK)
async def get_users(
    id: int | None = Query(None, description="Put user id to get info")
):
    if id is None:
        return temp_memory

    user = [info for info in temp_memory if info["id"] == id]

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user[0]


@app.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(payload: Create_user):
    # Check duplicate email
    for info in temp_memory:
        if info["email"] == payload.email:
            raise HTTPException(
                status_code=400,
                detail=f"User with email {payload.email} already exists",
            )

    # Generate unique ID
    user_id = random.randint(1, 100)
    while user_id in id_ref:
        user_id = random.randint(1, 100)

    id_ref.append(user_id)

    user = {
        "id": user_id,
        "name": payload.name,
        "email": payload.email,
    }

    temp_memory.append(user)
    return user
