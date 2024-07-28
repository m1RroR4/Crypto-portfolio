from datetime import date, time
from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr

class Token(BaseModel):
    symbol: str
    amount: float
    total_cost: float
    purchase_price: float
    purchase_date: date
    purchase_time: Optional[time] = time(0, 0)

class User(BaseModel):
    username: constr(min_length=3, max_length=50)
    _hashed_password: constr(min_length=8, max_length=50)
    email: Optional[EmailStr] = None
    portfolio: List[Token] = []
