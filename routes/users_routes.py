from fastapi import APIRouter
from models.users_models import User
from db.mongo import db,user  # <- db, not user
from bson import ObjectId

router = APIRouter()

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
