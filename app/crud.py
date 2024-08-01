from database import db
from models import User, Token


def create_user(user: User):
    try:
        db.users.insert_one(user.model_dump())
        return True
    except Exception as e:
        print(e)
        return False


def get_user(username: str):
    user = db.users.find_one({"username": username})
    return User(**user) if user else None


def update_user(username: str, user: User):
    try:
        db.users.update_one({"username": username}, {"$set": user.model_dump()})
        return True
    except Exception as e:
        print(e)
        return False


def delete_user(username: str):
    try:
        db.users.delete_one({"username": username})
        return True
    except Exception as e:
        print(e)
        return False


def add_token(username: str, token: Token):
    try:
        db.users.update_one({"username": username}, {"$push": {"portfolio": token.model_dump()}})
        return True
    except Exception as e:
        print(e)
        return False


def get_token(username: str, symbol: str):
    user = db.users.find_one({"username": username})
    if not user:
        raise ValueError(f"User '{username}' not found.")

    token = next((t for t in user["portfolio"] if t["symbol"] == symbol), None)
    if not token:
        return None

    try:
        return Token(**token)
    except Exception as e:
        print(f"Validation error: {e}")
        return None


def update_token(username: str, symbol: str, token: Token):
    try:
        db.users.update_one({"username": username, "portfolio.symbol": symbol},
                            {"$set": {"portfolio.$": token.model_dump()}})
        return True
    except Exception as e:
        print(e)
        return False


def delete_token(username: str, symbol: str):
    try:
        db.users.update_one({"username": username}, {"$pull": {"portfolio": {"symbol": symbol}}})
        return True
    except Exception as e:
        print(e)
        return False
