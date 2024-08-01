from datetime import date, time
from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr


class TokenPurchase(BaseModel):
    amount: float
    total_cost: float
    purchase_price: float
    purchase_date: date
    purchase_time: Optional[time] = time(0, 0)


class TokenSale(BaseModel):
    amount: float
    sale_price: float
    sale_date: date
    sale_time: Optional[time] = time(0, 0)


class Token(BaseModel):
    symbol: str
    amount: float
    total_cost: float
    average_purchase_price: float
    purchases: List[TokenPurchase] = []
    sales: List[TokenSale] = []


class User(BaseModel):
    username: constr(min_length=3, max_length=50)
    _hashed_password: constr(min_length=8, max_length=50)
    email: Optional[EmailStr] = None
    portfolio: List[Token] = []
