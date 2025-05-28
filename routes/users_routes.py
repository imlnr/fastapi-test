from fastapi import APIRouter, HTTPException
from models.users_models import User
from db.mongo import db,user  # <- db, not user
from bson import ObjectId

router = APIRouter()

@router.post("/register")
def register_user(user_data: User):
    try:
        # Check if user already exists
        existing_user = user.find_one({"email": user_data.email});
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Create new user
        user_dict = user_data.dict()
        result = user.insert_one(user_dict)
        
        # Get the created user
        userData = user.find_one({"_id": result.inserted_id})
        if "_id" in userData:
            userData["_id"] = str(userData["_id"])
            
        return {
            "message": "User registered successfully",
            "user": userData
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/users")
def create_user(singleUser: User):
    try:
        
        user_dict = singleUser.dict()
        result = user.insert_one(user_dict)
        userData = user.find_one({"_id":result.inserted_id})
        if "_id" in userData:
            userData["_id"] = str(userData["_id"])
        return {
            "message": "User created successfully",
            "user_id": userData
        }
    except Exception as e:
        return {"error": str(e)}
