from datetime import date, time
from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr

class Token(BaseModel):
    symbol: str
    amount: Optional[float] = None
    total_cost: Optional[float] = None
    purchase_price: Optional[float] = None
    purchase_date: date
    purchase_time: Optional[time] = time(0, 0)

    def __post_init__(self):
        if self.total_cost is None and self.purchase_price is None and self.amount is None:
            raise ValueError("At least one of total_cost, purchase_price, or amount must be provided.")

        if self.total_cost is None:
            if self.amount is not None and self.purchase_price is not None:
                self.total_cost = self.amount * self.purchase_price
            else:
                raise ValueError("Cannot calculate total_cost without amount and purchase_price.")

        if self.purchase_price is None:
            if self.total_cost is not None and self.amount is not None:
                self.purchase_price = self.total_cost / self.amount
            else:
                raise ValueError("Cannot calculate purchase_price without total_cost and amount.")

        if self.amount is None:
            if self.total_cost is not None and self.purchase_price is not None:
                self.amount = self.total_cost / self.purchase_price
            else:
                raise ValueError("Cannot calculate amount without total_cost and purchase_price.")

class User(BaseModel):
    username: constr(min_length=3, max_length=50)
    _hashed_password: constr(min_length=8, max_length=50)
    email: Optional[EmailStr] = None
    portfolio: List[Token] = []
