
from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.post("/register")
def register():
    return {"message": "User Registered"}
