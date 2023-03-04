
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class TransactionBase(BaseModel):
    amount: float
    description: str
    currency: str
    category: str
    payment_method: str
    is_egress: bool
    payment_date: Optional[datetime] = None


# Properties to receive via API on creation
class TransactionCreate(TransactionBase):
    pass


# Properties to receive via API on update
class TransactionUpdate(TransactionBase):
    pass


class TransactionInDBBase(TransactionBase):
    id: Optional[int] = None
    creation_date: Optional[datetime] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Transaction(TransactionInDBBase):
    pass


# Additional properties stored in DB
class TransactionInDB(TransactionInDBBase):
    id: int
    creation_date: datetime
